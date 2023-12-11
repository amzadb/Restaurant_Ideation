import os
from secret_key import openai_key
os.environ['OPENAI_API_KEY'] = openai_key

from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain

def generate_restaurant_name_and_menu_items(cuisine):
    llm = OpenAI(temperature=0.6)

    # restaurant name chain 
    prompt_template_name = PromptTemplate(
        input_variables = ['cuisine'],
        template = "I want to setup {cuisine} restaurant. Please suggest a name."
    )
    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="restaurant_name")

    # food menu items chain
    prompt_template_food = PromptTemplate(
        input_variables = ['restaurant_name'],
        template = "Suggest menu items for {restaurant_name}. Return it as comma separated list"
    )
    food_chain = LLMChain(llm=llm, prompt=prompt_template_food, output_key="menu_items")

    # Sequential chain
    chain = SequentialChain(
        chains = [name_chain, food_chain],
        input_variables = ['cuisine'],
        output_variables = ['restaurant_name', 'menu_items']
    )
    response = chain({'cuisine' : cuisine})

    return response

    # return {
    #     'restaurant_name' : 'Hyderabadi Delicious Delights',
    #     'menu_items' : 'Chicken Dum Biryani, Murg Malai Kabab, Chicken Tandoori, Chicken Tikka, Mutton Marag, Kadai Chicken'
    # }

if __name__ == "__main__":
    print(generate_restaurant_name_and_menu_items("Hyderabadi")) 