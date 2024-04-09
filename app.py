# -------------------------------------------------------------------------
# Prerequisites: The following three environment variables must be set:
# - APPLICATIONINSIGHTS_CONNECTION_STRING
# - OTEL_RESOURCE_ATTRIBUTES
# - OTEL_SERVICE_NAME
#
# Unknowns: 
# - How to redirect appinsight logs to console too.
#
# Resources:
# - https://learn.microsoft.com/en-us/azure/azure-monitor/app/opentelemetry-enable?tabs=aspnetcore
# - https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/monitor/azure-monitor-opentelemetry/samples/logging
# --------------------------------------------------------------------------

from logging import DEBUG, INFO, WARN, WARNING, ERROR, CRITICAL, getLogger, basicConfig

from azure.monitor.opentelemetry import configure_azure_monitor

configure_azure_monitor(
    # Set logger_name to the name of the logger you want to capture logging telemetry with
    logger_name="demo_logger",
)

# If you need to redirect logs to console, you can uncomment the line below
# basicConfig(filename="app.log")

# Logging calls with this logger will be tracked
logger = getLogger("demo_logger")
logger.setLevel(INFO)

#
# demo #1: sending data into appinsights 'traces' table
#
logger.debug("logger: debug log")
logger.info("logger: info log")
logger.warning("logger: warning log")
logger.error("logger: error log")
logger.critical("logger: critical log")

#
# demo #2: sending data into appinsights 'exceptions' table
#
# The following code will generate two pieces of exception telemetry
# that are identical in nature
try:
    val = 1 / 0
    print(val)
except ZeroDivisionError:
    logger.exception("Error: Division by zero")

try:
    val = 1 / 0
    print(val)
except ZeroDivisionError:
    logger.error("Error: Division by zero", stack_info=True, exc_info=True)

# Note: printf statements are NOT sent to appinsights
print("the end!")