from agency_swarm.agents import Agent


class ImageConverterCEO(Agent):
    def __init__(self):
        super().__init__(
            name="ImageConverterCEO",
            description="Oversees the entire image conversion process and coordinates with the ImageProcessor.",
            instructions="./instructions.md",
            files_folder="./files",
            schemas_folder="./schemas",
            tools=[],
            tools_folder="./tools",
            temperature=0.3,
            max_prompt_tokens=2048,
        )
        
    def response_validator(self, message):
        return message
