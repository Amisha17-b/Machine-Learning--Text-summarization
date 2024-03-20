from gensim.summarization.summarizer import summarize
def gensim_summary(input,ratio):
  summary = summarize(input,ratio/10)
  # print("".join(summary))
  return "".join(summary)