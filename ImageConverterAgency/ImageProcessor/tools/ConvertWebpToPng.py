from agency_swarm.tools import BaseTool
from pydantic import Field
from PIL import Image
import os

class ConvertWebpToPng(BaseTool):
    """
    This tool uses the PIL library to convert .webp images to .png format. It ensures that the converted images maintain high quality.
    """

    # Define the fields with descriptions using Pydantic Field
    webp_image_path: str = Field(
        ..., description="The file path of the .webp image to be converted to .png format."
    )

    def run(self):
        """
        The implementation of the run method, where the tool's main functionality is executed.
        This method converts the received .webp image file to .png format while maintaining high quality.
        """
        # Open the .webp image file
        with Image.open(self.webp_image_path) as img:
            # Convert the image to .png format
            png_image_path = self.webp_image_path.replace(".webp", ".png")
            img.save(png_image_path, "PNG", quality=100)

        # Return the path of the converted .png image file
        return f"Image converted to .png format and saved at: {png_image_path}"