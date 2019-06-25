
import uservoice

SUBDOMAIN_NAME = 'uservoice'
API_KEY = 'KbUgMTKwOovLVcNnvI1DQ'
API_SECRET = 'QZFsHiTVaTjRAdIvMPw6VI2iOASCXrIGvOpKcxWnLQ'

client = uservoice.Client(SUBDOMAIN_NAME, API_KEY, API_SECRET)
with client.login_as_owner() as owner:
    user = owner.get("/api/v1/users/current")
    print(user)

