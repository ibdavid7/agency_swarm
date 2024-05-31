from agency_swarm.tools import BaseTool
from pydantic import Field

class HandleConversionIssues(BaseTool):
    """
    This tool handles any issues that arise during the conversion process and reports them to the ImageConverterCEO agent. It accepts the error message as input and sends it to the ImageConverterCEO agent.
    """

    # Define the fields with descriptions using Pydantic Field
    error_message: str = Field(
        ..., description="The error message to be reported to the ImageConverterCEO agent."
    )

    def run(self):
        """
        The implementation of the run method, where the tool's main functionality is executed.
        This method sends the error message to the ImageConverterCEO agent.
        """
        # Here, we assume that the ImageConverterCEO agent has a method to receive error messages.
        # For the purpose of this example, we'll just print the error message.
        # In a real implementation, you would replace this with the actual communication logic.
        
        # Example: ImageConverterCEO.receive_error(self.error_message)
        print(f"Reporting error to ImageConverterCEO: {self.error_message}")

        # Return a confirmation message
        return f"Error reported to ImageConverterCEO: {self.error_message}"