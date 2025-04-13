# Markdown Generator API

A FastAPI-based service that converts web pages to markdown format.

## Features

- Convert any webpage URL to markdown format
- Simple and easy-to-use API
- Error handling for invalid URLs or conversion failures
- Health check endpoint for monitoring

## Installation

1. Clone this repository
2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Running the Server

Start the development server:
```bash
fastapi dev main.py
```

The server will start at `http://localhost:8000`

## API Endpoints

### Generate Markdown
- **Endpoint**: `/generate-md`
- **Method**: POST
- **Request Body**:
```json
{
    "url": "https://example.com"
}
```
- **Response**:
```json
{
    "markdown": "# Generated Markdown Content..."
}
```

### Health Check
- **Endpoint**: `/health`
- **Method**: GET
- **Response**:
```json
{
    "status": "ok"
}
```

## Example Usage

Using curl:
```bash
# Generate markdown from a URL
curl -X POST "http://localhost:8000/generate-md" \
     -H "Content-Type: application/json" \
     -d '{"url": "https://example.com"}'

# Check server health
curl "http://localhost:8000/health"
```

## Error Handling

If an error occurs during conversion, the API will return an error message:
```json
{
    "error": "Error message describing what went wrong"
}
```

## Dependencies

- FastAPI
- Uvicorn
- MarkItDown
- Pydantic

## Deployment on Vercel

This application is configured for deployment on Vercel. To deploy:

1. Install the Vercel CLI:
```bash
npm install -g vercel
```

2. Login to your Vercel account:
```bash
vercel login
```

3. Deploy the application:
```bash
vercel
```

4. Follow the prompts to complete the deployment.

The application will be deployed and you'll receive a URL where your API is accessible.

### Environment Variables

No environment variables are required for basic functionality. If you need to configure any additional settings, you can add them through the Vercel dashboard.

### Custom Domain

You can set up a custom domain through the Vercel dashboard after deployment. 