import hvac

# Create a client to interact with Vault
client = hvac.Client(
    url='http://127.0.0.1:8200',
    token='s.YOUR_VAULT_TOKEN'
)

# Check if the client is authenticated
if client.is_authenticated():
    print("Successfully authenticated with Vault")

    # Write a secret
    client.secrets.kv.v2.create_or_update_secret(
        path='secret/data/my-secret',
        secret={'username': 'my-username', 'password': 'my-password'}
    )
    print("Secret written to Vault")

    # Read the secret back
    read_secret_result = client.secrets.kv.v2.read_secret_version(path='secret/data/my-secret')
    secret_data = read_secret_result['data']['data']
    print(f"Username: {secret_data['username']}")
    print(f"Password: {secret_data['password']}")

    # Delete the secret
    client.secrets.kv.v2.delete_metadata_and_all_versions(path='secret/data/my-secret')
    print("Secret deleted from Vault")

else:
    print("Failed to authenticate with Vault")
