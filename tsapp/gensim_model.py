from gensim.summarization.summarizer import summarize
"""
    Generates a summary using Gensim's summarization module.
    
    Args:
        input (str): The input text to be summarized.
        ratio (float): The ratio of the summary length to the original text length.
        
    Returns:
        str: The generated summary.
    """
# Generate the summary using Gensim's summarize function
def gensim_summary(input,ratio):
   # Join the summary sentences into a single string
  summary = summarize(input,ratio/10)
  # print("".join(summary))
  return "".join(summary)