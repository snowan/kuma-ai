import phoenix as px
import os
from phoenix.otel import register

# For Google Generative AI instrumentation - install with:
# pip install openinference-instrumentation-google-genai
from openinference.instrumentation.google_genai import GoogleGenAIInstrumentor

# Semantic conventions
from openinference.semconv.trace import SpanAttributes

# OpenTelemetry imports
from opentelemetry.trace import Status, StatusCode, TracerProvider
# OR if you need the trace module:
from opentelemetry import trace

# Test the imports
if __name__ == "__main__":
    print("✓ All imports successful!")
    print(f"Phoenix version: {px.__version__}")