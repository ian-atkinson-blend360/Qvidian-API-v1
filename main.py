import os

import qvidianapi

USERNAME = os.environ.get("QVIDIAN_USERNAME")
PASSWORD = os.environ.get("QVIDIAN_PASSWORD")


def test_auth(username=USERNAME, password=PASSWORD):
    auth = qvidianapi.QvidianAuthentication()

    auth.Connect(userName=username, password=password)

    common_client = qvidianapi.Common(auth)

    common_client.HasPermissions("AllowPreviewHTML")

    print(common_client.HasPermissionsResponse)


if __name__ == "__main__":
    test_auth()
