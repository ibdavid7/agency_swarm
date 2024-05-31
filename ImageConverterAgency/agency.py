from agency_swarm import Agency
from ImageProcessor import ImageProcessor
from ImageConverterCEO import ImageConverterCEO

ceo = ImageConverterCEO()
processor = ImageProcessor()

agency = Agency([ceo, processor, [ceo, processor]],
                shared_instructions='./agency_manifesto.md',  # shared instructions for all agents
                max_prompt_tokens=25000,  # default tokens in conversation for all agents
                temperature=0.3,  # default temperature for all agents
                )

if __name__ == '__main__':
    agency.demo_gradio()