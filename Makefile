.PHONY: create_virtual_env build_images run_infra

# Step 1: Create Virtual Environment
virtual_env:
	@echo "Creating virtual environment..."
	./scripts/create_virtual_env.sh

# Step 2: Build Images
build_images:
	@echo "Building Spark and Python images..."
	docker build -t spark-image -f Dockerfile_spark .
	docker build -t python-image -f Dockerfile_python .

# Step 3: Run Infrastructure
run_infra:
	@echo "Running infrastructure..."
	docker-compose up -d
