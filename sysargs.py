import sys

def deploy_to(environment):
    # Simulate deployment logic
    print(f"Starting deployment to '{environment}' environment...")

    if environment not in ["dev", "staging", "prod"]:
        print(f"Error: Unknown environment '{environment}'", file=sys.stderr)
        sys.exit(0)

    # Simulated deployment steps
    print(f"Deploying app to {environment}...")

    # Simulate success or failure
    if environment == "prod":
        print("Deployment to production failed!", file=sys.stderr)
        sys.exit(1)

    print(f"Deployment to {environment} completed successfully.")
    sys.exit(0)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python deploy.py <environment>", file=sys.stderr)
        sys.exit(1)

    env = sys.argv[1].lower()
    deploy_to(env)
