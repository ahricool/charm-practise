from tests import factories
from tests.ci.functional.api import factories as api_factories

# curl --location --request GET 'https://tai-api.company.com/v1.2/apps/google-play/app/20600001191051/reviews?page_size=50&countries=US' \
# --header 'Authorization: Bearer 6a7a558ecdc18f110087c9a38b4df28de019f083' \
# --header 'X-AA-DMS-NAMESPACE: taiaaconnsalesgoservice264' \
# --header 'X-AA-DMS-NAMESPACE: taiaaconniaagoservice222' \
# --header 'X-AA-DMS-NAMESPACE: taiaaconngagoservice198'

u,c= factories.create_user_and_client()
user_key = api_factories.UserKeyFactory(user=u)
t=user_key.token
ap=factories.create_gp_appcare(u)
extra={}
extra["HTTP_AUTHORIZATION"]="Bearer "+t
path="/v1.2/apps/google-play/app/20600001191051/reviews?page_size=50&countries=US"
d=c.get(path,{},**extra)