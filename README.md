# FastAPI Token Cache

## Project Description

This FastAPI application implements a local caching mechanism for authentication tokens to reduce latency and improve API performance. The cache follows a First-In-First-Out (FIFO) eviction strategy and supports adding and retrieving tokens.

## Features

- **Set Token**: Endpoint to add tokens to the cache.
- **Get Token**: Endpoint to retrieve tokens from the cache.
- **FIFO Eviction**: Oldest tokens are removed when the cache reaches its maximum size.

## Setup Instructions

### Prerequisites

Ensure you have Python 3.8 or later installed.

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/prakashdatasintist/Symplique_assignment.git
   cd your-repo
   ```
2. **Create a virtual environment (optional but recommended):**

   ```bash
   python -m venv venv
   ```
3. **Activate the virtual environment:**

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```
4. **Install the required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the FastAPI application:**

   ```bash
   uvicorn main:app --reload
   ```

   This will start the FastAPI server at `http://127.0.0.1:8000`.
2. **Access the API Documentation:**

   Open your web browser and navigate to `http://127.0.0.1:8000/docs` to view the interactive API documentation.

## Endpoints

- **POST /set_token/**

  - **Description:** Adds a token to the cache.
  - **Parameters:**
    - `token` (query parameter): The token to be added.
  - **Response:** `{"message": "Token added to cache"}`
- **GET /get_token/**

  - **Description:** Retrieves a token from the cache.
  - **Parameters:**
    - `token` (query parameter): The token to be retrieved.
  - **Response:**
    - If token exists: `{"token": "<token>"}`
    - If token does not exist: `{"detail": "Token not found in cache"}`

## Testing

### Running Tests

1. **Install testing dependencies:**

   ```bash
   pip install pytest httpx
   ```
2. **Run the tests:**

   ```bash
   pytest
   ```

   To run specific tests, use:

   ```bash
   pytest -k "test_set_token or test_get_token"
   ```

## Contributing

Feel free to open issues or submit pull requests to improve the application. Please ensure that any contributions adhere to the project's coding standards and include appropriate tests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

For any questions or comments, please contact [prakashmkumbar04@gmail.com](mailto:your-email@example.com).
