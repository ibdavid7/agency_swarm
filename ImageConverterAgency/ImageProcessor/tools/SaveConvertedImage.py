from agency_swarm.tools import BaseTool
from pydantic import Field
import shutil

class SaveConvertedImage(BaseTool):
    """
    This tool saves the converted .png images to the specified location. It accepts the converted image file and the target location as input and saves the image accordingly.
    """

    # Define the fields with descriptions using Pydantic Field
    converted_image_path: str = Field(
        ..., description="The file path of the converted .png image to be saved."
    )
    target_location: str = Field(
        ..., description="The target location where the .png image will be saved."
    )

    def run(self):
        """
        The implementation of the run method, where the tool's main functionality is executed.
        This method saves the converted .png image file to the specified target location.
        """
        # Copy the converted image to the target location
        shutil.copy(self.converted_image_path, self.target_location)

        # Return the path of the saved image file
        return f"Converted .png image saved at: {self.target_location}"