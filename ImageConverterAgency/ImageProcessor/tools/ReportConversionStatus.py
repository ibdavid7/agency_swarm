from agency_swarm.tools import BaseTool
from pydantic import Field

class ReportConversionStatus(BaseTool):
    """
    This tool reports the status of the conversion process to the ImageConverterCEO agent. It accepts the status message as input and sends it to the ImageConverterCEO agent.
    """

    # Define the fields with descriptions using Pydantic Field
    status_message: str = Field(
        ..., description="The status message to be reported to the ImageConverterCEO agent."
    )

    def run(self):
        """
        The implementation of the run method, where the tool's main functionality is executed.
        This method sends the status message to the ImageConverterCEO agent.
        """
        # Here, we assume that the ImageConverterCEO agent has a method to receive status messages.
        # For the purpose of this example, we'll just print the status message.
        # In a real implementation, you would replace this with the actual communication logic.
        
        # Example: ImageConverterCEO.receive_status(self.status_message)
        print(f"Reporting to ImageConverterCEO: {self.status_message}")

        # Return a confirmation message
        return f"Status reported to ImageConverterCEO: {self.status_message}"