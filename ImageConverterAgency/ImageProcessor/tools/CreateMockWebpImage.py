from agency_swarm.tools import BaseTool
from pydantic import Field
from PIL import Image
import os

class CreateMockWebpImage(BaseTool):
    """
    This tool creates a mock .webp image file for testing purposes. It generates a simple image and saves it in .webp format.
    """

    # Define the fields with descriptions using Pydantic Field
    image_width: int = Field(
        100, description="The width of the mock image to be created."
    )
    image_height: int = Field(
        100, description="The height of the mock image to be created."
    )
    image_color: str = Field(
        "blue", description="The color of the mock image to be created."
    )
    output_path: str = Field(
        "mock_image.webp", description="The file path where the mock .webp image will be saved."
    )

    def run(self):
        """
        The implementation of the run method, where the tool's main functionality is executed.
        This method generates a simple image and saves it in .webp format.
        """
        # Create a new image with the specified dimensions and color
        img = Image.new("RGB", (self.image_width, self.image_height), self.image_color)
        
        # Save the image in .webp format
        img.save(self.output_path, "WEBP")

        # Return the path of the created mock .webp image file
        return f"Mock .webp image created and saved at: {self.output_path}"