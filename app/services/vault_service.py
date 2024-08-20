import hvac

# Create a client to interact with Vault
client = hvac.Client(
    url='http://127.0.0.1:8200',
    token=''
)

client.secrets.kv.v2.configure(
    max_versions=20,
    mount_point='kv',
)

# Check if the client is authenticated
if client.is_authenticated():
    print("Successfully authenticated with Vault")

    # Write a secret
    client.secrets.kv.v2.create_or_update_secret(
        path='hello',
        secret={'username': 'foo', 'password': 'bar'}
    )
    print("Secret written to Vault")

    # Read the secret back
    read_secret_result = client.secrets.kv.v2.read_secret_version(path='hello')
    secret_data = read_secret_result['data']['data']
    print(f"Username: {secret_data['username']}")
    print(f"Password: {secret_data['password']}")

    # Delete the secret
    client.secrets.kv.v2.delete_metadata_and_all_versions(path='hello')
    print("Secret deleted from Vault")

else:
    print("Failed to authenticate with Vault")
