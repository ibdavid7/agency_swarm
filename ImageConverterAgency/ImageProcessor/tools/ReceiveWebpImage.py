from agency_swarm.tools import BaseTool
from pydantic import Field
import os
import tempfile

class ReceiveWebpImage(BaseTool):
    """
    This tool receives .webp images for conversion. It accepts the image file as input and stores it temporarily for processing.
    """

    # Define the fields with descriptions using Pydantic Field
    image_file: bytes = Field(
        ..., description="The .webp image file to be received and stored temporarily for processing."
    )

    def run(self):
        """
        The implementation of the run method, where the tool's main functionality is executed.
        This method stores the received .webp image file temporarily for further processing.
        """
        # Create a temporary file to store the image
        with tempfile.NamedTemporaryFile(delete=False, suffix=".webp") as temp_file:
            temp_file.write(self.image_file)
            temp_file_path = temp_file.name

        # Return the path of the temporarily stored image file
        return f"Image stored temporarily at: {temp_file_path}"