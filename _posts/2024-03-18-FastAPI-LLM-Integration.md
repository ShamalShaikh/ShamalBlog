---
title: "Building Production-Ready LLM Applications with FastAPI"
date: 2025-02-05 12:00:00 +/-TTTT
categories: [Tutorials, Backend]
tags: [fastapi, python, llm, api-design]
image:
  src: "/ShamalBlog/images/tutorials/fastapi-llm.jpg"
  alt: "FastAPI LLM Integration"
---

## Building Scalable LLM Applications with FastAPI

In this tutorial, I'll show you how to build a production-ready LLM application using FastAPI, focusing on best practices and performance optimization.

### Setting Up the Project

```python
from fastapi import FastAPI, HTTPException, BackgroundTasks
from pydantic import BaseModel
from typing import List, Optional
import asyncio
import logging

# Initialize FastAPI app with metadata
app = FastAPI(
    title="LLM API Service",
    description="Production-ready LLM integration",
    version="1.0.0"
)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
```

### Request/Response Models

```python
class LLMRequest(BaseModel):
    prompt: str
    max_tokens: Optional[int] = 100
    temperature: Optional[float] = 0.7
    stream: Optional[bool] = False

class LLMResponse(BaseModel):
    text: str
    tokens_used: int
    model_version: str
```

### Implementing Rate Limiting

```python
from fastapi import Depends
from fastapi.middleware.throttling import ThrottlingMiddleware

# Custom rate limiter
class RateLimiter:
    def __init__(self, max_requests: int, window_seconds: int):
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.requests = {}

    async def check(self, client_id: str) -> bool:
        now = time.time()
        if client_id not in self.requests:
            self.requests[client_id] = []
        
        # Clean old requests
        self.requests[client_id] = [
            req_time for req_time in self.requests[client_id]
            if now - req_time < self.window_seconds
        ]
        
        if len(self.requests[client_id]) >= self.max_requests:
            return False
            
        self.requests[client_id].append(now)
        return True
```

### Implementing the LLM Service

```python
class LLMService:
    def __init__(self):
        self.model = load_llm_model()  # Your model loading logic
        self._request_queue = asyncio.Queue()
        self._batch_size = 5
        self._processing_task = asyncio.create_task(self._process_queue())

    async def generate(self, request: LLMRequest) -> LLMResponse:
        # Add request to queue
        future = asyncio.Future()
        await self._request_queue.put((request, future))
        return await future

    async def _process_queue(self):
        while True:
            batch = []
            try:
                # Collect batch_size requests or wait for timeout
                while len(batch) < self._batch_size:
                    try:
                        request, future = await asyncio.wait_for(
                            self._request_queue.get(),
                            timeout=0.1
                        )
                        batch.append((request, future))
                    except asyncio.TimeoutError:
                        break

                if batch:
                    # Process batch
                    responses = await self._process_batch(batch)
                    # Set results
                    for (_, future), response in zip(batch, responses):
                        future.set_result(response)

            except Exception as e:
                logger.error(f"Error processing batch: {e}")
                for _, future in batch:
                    if not future.done():
                        future.set_exception(e)
```

### API Endpoints

```python
@app.post("/generate", response_model=LLMResponse)
async def generate_text(
    request: LLMRequest,
    background_tasks: BackgroundTasks,
    llm_service: LLMService = Depends(get_llm_service)
):
    try:
        response = await llm_service.generate(request)
        
        # Add background task for analytics
        background_tasks.add_task(
            log_request_metrics,
            request=request,
            response=response
        )
        
        return response
    except Exception as e:
        logger.error(f"Error generating text: {e}")
        raise HTTPException(status_code=500, detail=str(e))
```

### Error Handling & Monitoring

```python
@app.middleware("http")
async def add_monitoring(request: Request, call_next):
    start_time = time.time()
    
    try:
        response = await call_next(request)
        
        # Record metrics
        duration = time.time() - start_time
        status_code = response.status_code
        
        # Log metrics (replace with your monitoring solution)
        logger.info(
            f"Request processed: duration={duration:.2f}s, "
            f"status={status_code}"
        )
        
        return response
    except Exception as e:
        logger.error(f"Request failed: {e}")
        raise
```

## Best Practices & Tips

1. **Batch Processing**
   - Group requests for better throughput
   - Implement smart timeouts
   - Handle partial batch failures

2. **Error Handling**
   - Implement proper error types
   - Add detailed logging
   - Use background tasks for metrics

3. **Performance Optimization**
   - Use connection pooling
   - Implement caching
   - Monitor resource usage

## Testing the Application

```python
from fastapi.testclient import TestClient
import pytest

@pytest.fixture
def client():
    return TestClient(app)

def test_generate_text(client):
    response = client.post(
        "/generate",
        json={
            "prompt": "Test prompt",
            "max_tokens": 50
        }
    )
    assert response.status_code == 200
    assert "text" in response.json()
```

[View complete code on GitHub →](https://github.com/yourusername/fastapi-llm-tutorial) 