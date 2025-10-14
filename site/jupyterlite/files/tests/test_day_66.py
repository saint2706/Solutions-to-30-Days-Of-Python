import os
import sys
from pathlib import Path

sys.path.insert(0, os.path.abspath(Path(__file__).resolve().parents[1]))

from Day_66_Model_Deployment_and_Serving import solutions  # noqa: E402


def test_rest_adapter_returns_expected_schema():
    endpoint = solutions.fastapi_rest_adapter(solutions.averaged_ensembled_model)
    payload = {"instances": [0.2, 0.4, 0.6]}
    response = endpoint(payload)
    solutions.ensure_response_schema(response)
    assert response["metadata"]["transport"] == "REST"


def test_grpc_adapter_streams_multiple_responses():
    handler = solutions.grpc_streaming_adapter(solutions.averaged_ensembled_model)
    payloads = [{"instances": [0.1, 0.3]}, {"instances": [0.5, 0.7]}]
    responses = list(handler(payloads))
    assert len(responses) == 2
    for response in responses:
        solutions.ensure_response_schema(response)
        assert response["metadata"]["transport"] == "gRPC"


def test_synthetic_load_test_reports_success():
    endpoint = solutions.fastapi_rest_adapter(solutions.averaged_ensembled_model)
    payloads = [{"instances": [0.1, 0.2, 0.3]} for _ in range(5)]
    result = solutions.run_synthetic_load_test(endpoint, payloads, warmups=2)
    assert result.success_rate == 1.0
    assert result.avg_latency >= 0.0
    assert result.throughput > 0.0
