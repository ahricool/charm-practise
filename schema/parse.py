# Copyright (c) 2019 App Annie Inc. All rights reserved.
# coding=utf-8

import csv
import datetime
import glob
import json
import logging
import os

# from django.conf import settings

# from company.utils.datetime import string_to_date, gen_dates_in_range, date_to_string
# from common.s3 import secure_s3_storage
# from webanalytics.services.mongo.ga.constants import GADocumentType
# from webanalytics.tasks.in_app_analytics.firebase.constants import (
#     GRANULARITY_DAILY, GRANULARITY_WEEKLY, GRANULARITY_MONTHLY,
#     MULTI_LAN_KEYWORD_ACTIVE_USER, MULTI_LAN_KEYWORD_DAILY_USER_ENGAGEMENT, MULTI_LAN_KEYWORD_AUDIENCE,
#     ACTIVE_USER_ROW_IDENTIFIERS, DAILY_USER_ENGAGEMENT_ROW_IDENTIFIERS, AUDIENCE_ROW_IDENTIFIERS
# )
# from webanalytics.tasks.in_app_analytics.firebase.exception import FirebaseUnsupportedLanguageException

logger = logging.getLogger(__name__)

GRANULARITY_DAILY = 'daily'
GRANULARITY_WEEKLY = 'weekly'
GRANULARITY_MONTHLY = 'monthly'

MULTI_LAN_KEYWORD_ACTIVE_USER = [
    '# Active users #',
    '# アクティブ ユーザー #',
    '# 활성 사용자 #',
    '# Utilisateurs actifs #',  # French
    '# Aktive Nutzer #',  # German
    '# 活跃用户 #',
    '# Usuarios activos #',  # Spanish
    '# Активные пользователи #',  # Russian
    '# Utenti attivi #',  # Italian
    '# Actieve gebruikers #',  # Dutch
    '# Etkin kullanÄ±cÄ± sayÄ±sÄ± #',  # Turkish
    '# Etkin kullan\xc4\xb1c\xc4\xb1 say\xc4\xb1s\xc4\xb1 #',  # Turkish
    '# Aktywni uÅ¼ytkownicy #',  # Polish
    '# Aktywni u\xc5\xbcytkownicy #',  # Polish
    '# UsuÃ¡rios ativos #',  # Portugal
    '# Usu\xc3\xa1rios ativos #',  # Portugal
    '# Pengguna aktif #',  # Indonesian
]
MULTI_LAN_KEYWORD_DAILY_USER_ENGAGEMENT = [
    '# Daily user engagement #',
    '# 1 日のユーザー エンゲージメント #',
    '# 일일 사용자 참여 #',
    '# Engagement quotidien des utilisateurs #',  # French
    '# Tägliche Nutzerinteraktionen #',  # German
    '# TÃ¤gliches Nutzer-Engagement #',  # German
    '# 用户每日互动时长 #',
    '# Interacción diaria de los usuarios #',  # Spanish
    '# Длительность взаимодействия с пользователями в день #',  # Russian
    '# Coinvolgimento utente giornaliero #',  # Italian
    '# Dagelijkse betrokkenheid van gebruikers #',  # Dutch
    '# GÃ¼nlÃ¼k kullanÄ±cÄ± etkileÅimi #',  # Turkish
    '# G\xc3\xbcnl\xc3\xbck kullan\xc4\xb1c\xc4\xb1 etkile\xc5\x9fimi #',  # Turkish
    '# Dzienne zaangaÅ¼owanie uÅ¼ytkownikÃ³w #',  # Polish
    '# Dzienne zaanga\xc5\xbcowanie u\xc5\xbcytkownik\xc3\xb3w #',  # Polish
    '# Engajamento diÃ¡rio do usuÃ¡rio #',  # Portugal
    '# Engajamento di\xc3\xa1rio do usu\xc3\xa1rio #',  # Portugal
    '# Interaksi pengguna harian #',  # Indonesian
]
MULTI_LAN_KEYWORD_AUDIENCE = [
    '# Audience #',
    '# オーディエンス #',
    '# 잠재고객 #',
    '# Audience #',  # French
    '# Zielgruppe #',  # German
    '# 受众群体 #',
    '# Audiencia #',  # Spanish
    '# Аудитория #',  # Russian
    '# Segmento di pubblico #',  # Italian
    '# Doelgroep #',  # Dutch
    '# Kitle #',  # Turkish (this is weird)
    '# Odbiorcy #',  # Polish
    '# PÃºblico-alvo #',  # Portugal
    '# P\xc3\xbablico-alvo #',  # Portugal
    '# Audiens #',  # Indonesian
]

ACTIVE_USER_ROW_IDENTIFIERS = ['N', 'Tag']
DAILY_USER_ENGAGEMENT_ROW_IDENTIFIERS = ['N', 'Tag', 'Hari ke-n', 'Page path and screen class']
AUDIENCE_ROW_IDENTIFIERS = ['N', 'ID', 'Идентификатор страны']


class FirebaseUnsupportedLanguageException(Exception):
    pass


def gen_dates_in_range(begin_date, end_date, step=1):
    """
    Generate date range from begin_date to end_date.

    :param datetime.date begin_date: the begin date
    :param datetime.date end_date: the end date
    :param int step: the interval of the date range
    :returns: the generator
    :rtype: generator

    Example::

    >>> import datetime
    >>> begin_date = datetime.date(2015, 07, 20)
    >>> end_date = datetime.date(2015, 07, 25)
    >>> result = gen_dates_in_range(begin_date, end_date)
    >>> list(result)
    >>> [datetime.date(2015, 7, 20), datetime.date(2015, 7, 21) ... ]
    """
    dt = begin_date
    while dt <= end_date:
        yield dt
        dt += datetime.timedelta(days=step)


def string_to_date(date_str, pattern='%Y-%m-%d'):
    """
    Get the date object in terms of its string format.

    :param str date_str: date string
    :param str pattern: pattern of date string
    :returns: date object
    :rtype: datetime.date
    """
    return datetime.datetime.strptime(date_str, pattern).date()


def date_to_string(date, pattern='%Y-%m-%d'):
    """
    Convert date object to date_str.

    :param datetime.date date: date object
    :param str pattern: pattern of date string
    :returns: string format of the date
    :rtype: str
    """
    if date and isinstance(date, datetime.date) or \
        isinstance(date, datetime.datetime):
        return date.strftime(pattern)

    return date


class FirebaseParserFeeder(object):
    def __init__(self, user_id, appcare_id, abs_user_dir, begin_date, end_date, granularity):
        self.user_id = user_id
        self.appcare_id = appcare_id
        self.abs_user_dir = abs_user_dir
        self.begin_date = begin_date[0] if isinstance(begin_date, list) else begin_date
        self.end_date = end_date
        self.granularity = granularity
        self.is_from_s3 = True
        # self.bucket_name = settings.FIREBASE_REPORT_BUCKET

    def feed(self):
        return self.feed_from_local()
        # if self.is_from_s3:
        #     return self.feed_from_s3()
        # else:
        #     return self.feed_from_local()

    def feed_from_local(self):
        items_in_local_dir = os.listdir(self.abs_user_dir)
        for item in items_in_local_dir:
            item_path = os.path.join(self.abs_user_dir, item)
            if os.path.isdir(item_path):
                csv_files = glob.glob(os.path.join(
                    item_path, '*', '*', '*', '*', '*', 'data-export.csv'))
                if csv_files:
                    for csv_file in csv_files:
                        yield csv_file

    # def feed_from_s3(self):
    #     if not os.path.exists(self.abs_user_dir):
    #         os.makedirs(self.abs_user_dir)
    #
    #     common_s3_prefix = '{}/{}'.format(str(self.user_id), str(self.appcare_id))
    #     dates = [date_to_string(date, '%Y%m%d') for date in self.get_dates_in_range()]
    #     expected_keys = ['{}/{}/{}_{}.zip'.format(self.user_id, self.appcare_id, self.granularity, date) for date in
    #                      dates]
    #
    #     for s3_key in secure_s3_storage.list(self.bucket_name, common_s3_prefix):
    #         if s3_key in expected_keys:
    #             local_zipfile = os.path.join(self.abs_user_dir, os.path.basename(s3_key))
    #             secure_s3_storage.download_file(self.bucket_name, s3_key, local_zipfile)
    #             z = zipfile.ZipFile(local_zipfile)
    #             z.extractall(self.abs_user_dir)
    #             os.unlink(local_zipfile)
    #
    #     csv_files = glob.glob(
    #         os.path.join(self.abs_user_dir, '*', '*', '*', '*', 'data-export.csv'))
    #     if csv_files:
    #         for csv_file in csv_files:
    #             yield csv_file

    def get_dates_in_range(self):
        begin_date = string_to_date(self.begin_date)
        end_date = string_to_date(self.end_date)
        dates = gen_dates_in_range(begin_date, end_date)
        if self.granularity == GRANULARITY_DAILY:
            return dates
        elif self.granularity == GRANULARITY_WEEKLY:
            return list(filter(lambda date: date.weekday() == 6, dates))
        elif self.granularity == GRANULARITY_MONTHLY:
            return list(filter(lambda date: date.day == 1, dates))


class FirebaseFileParser(object):

    def __init__(self, granularity, user_id, appcare_id):
        self.granularity = granularity
        self.appcare_id = appcare_id
        self.user_id = user_id
        self.data = {
            self.active_user_key: None,
            'avg_daily_user_engagement': None,
            'avg_session_duration': 0,
            'total_sessions': 0,
            'total_session_duration': 0,
            'total_sessions_by_country': {}
        }
        self.unsupported_language = False

    @property
    def active_user_key(self):
        if self.granularity == GRANULARITY_DAILY:
            return 'DAU'
        elif self.granularity == GRANULARITY_WEEKLY:
            return 'WAU'
        elif self.granularity == GRANULARITY_MONTHLY:
            return 'MAU'

    def get_no_breakdown_data(self):
        total_sessions = 0
        for _, session in self.data['total_sessions_by_country'].items():
            total_sessions += int(session['total_sessions'])

        avg_daily_user_engagement = self.data.get('avg_daily_user_engagement') or 0
        avg_session_duration = 0

        _active_user = self.data.get(self.active_user_key) or 0
        if total_sessions:
            avg_session_duration = avg_daily_user_engagement * _active_user / total_sessions

        total_session_duration = _active_user * avg_daily_user_engagement

        data = {
            'avg_daily_user_engagement': avg_daily_user_engagement,
            'avg_session_duration': avg_session_duration,
            'total_sessions': total_sessions,
            'total_session_duration': total_session_duration,
            self.active_user_key: _active_user,
        }
        no_breakdown_data = {k: v for k, v in data.items() if v}
        if no_breakdown_data:
            no_breakdown_data.update({
                'type': 1
            })
        return no_breakdown_data

    def get_breakdown_data(self):
        if self.data['total_sessions_by_country']:
            return {
                "country": self.data['total_sessions_by_country'],
                'type': 2
            }
        return {}

    def parse(self, filename):
        active_user_line_num = None
        active_user_row_num = 3
        session_line_start = -1
        daily_user_engagement_line_start = -1
        avg_daily_user_engagement_list = []

        finding_active_user = False
        finding_daily_user_engagement = False
        finding_sessions = False
        import ipdb;
        ipdb.set_trace();
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            if self.granularity == GRANULARITY_DAILY:
                active_user_row_num = 3
            elif self.granularity == GRANULARITY_WEEKLY:
                active_user_row_num = 2
            elif self.granularity == GRANULARITY_MONTHLY:
                active_user_row_num = 1

            for row in reader:
                # Active users
                if finding_active_user:
                    if len(row) > 1 and any([s in row[0].strip() for s in ACTIVE_USER_ROW_IDENTIFIERS]):
                        active_user_line_num = reader.line_num + 1
                        finding_active_user = False
                else:
                    if row and row[0].strip() in MULTI_LAN_KEYWORD_ACTIVE_USER:
                        finding_active_user = True
                    if active_user_line_num == reader.line_num:
                        self.data[self.active_user_key] = int(
                            row[active_user_row_num]) if len(row) > active_user_row_num else 0

                # Daily user engagement
                if finding_daily_user_engagement:
                    if len(row) > 1 and any([s in row[0].strip() for s in DAILY_USER_ENGAGEMENT_ROW_IDENTIFIERS]):
                        daily_user_engagement_line_start = reader.line_num + 1
                        finding_daily_user_engagement = False
                else:
                    if row and row[0].strip() in MULTI_LAN_KEYWORD_DAILY_USER_ENGAGEMENT and \
                        daily_user_engagement_line_start == -1:
                        finding_daily_user_engagement = True
                    if daily_user_engagement_line_start > 0 and not row:
                        daily_user_engagement_line_start = -2
                        if avg_daily_user_engagement_list:
                            self.data['avg_daily_user_engagement'] = sum(
                                avg_daily_user_engagement_list) / len(avg_daily_user_engagement_list)
                    if reader.line_num >= daily_user_engagement_line_start > 0:
                        avg_daily_user_engagement_list.append(float(row[1]))

                # Sessions (country breakdown)
                if finding_sessions:
                    if len(row) > 1 and any([s in row[0].strip() for s in AUDIENCE_ROW_IDENTIFIERS]):
                        session_line_start = reader.line_num + 1
                        finding_sessions = False
                else:
                    if row and row[0].strip() in MULTI_LAN_KEYWORD_AUDIENCE and session_line_start == -1:
                        finding_sessions = True
                    if session_line_start > 0 and not row:
                        session_line_start = -2
                    if reader.line_num >= session_line_start > 0:
                        if int(row[1]):
                            self.data['total_sessions_by_country'][row[0]] = {
                                "total_sessions": int(row[1])}

            if session_line_start == -1 and daily_user_engagement_line_start == -1:
                f.seek(0)
                rows = [r[0] for r in reader if r and r[0].strip().startswith('#') and r[0].strip().endswith('#')]
                logger.warning('[Firebase Unsupported Report] user_id:{},appcare_id:{},content:{}'
                               .format(self.user_id, self.appcare_id, rows))
                raise FirebaseUnsupportedLanguageException(json.dumps(rows))


def main():
    feeder = FirebaseParserFeeder(
        1190204, 646486, '/Users/huazhang/workspace/company/aa/tmp', '2020-04-16', '2020-04-18', GRANULARITY_DAILY
    )
    feeder.is_from_local = True
    for csv_file in feeder.feed():
        parser = FirebaseFileParser(granularity=GRANULARITY_DAILY, user_id=1190204, appcare_id=646486)
        parser.parse(csv_file)

        print(parser.data)


if __name__ == '__main__':
    main()

