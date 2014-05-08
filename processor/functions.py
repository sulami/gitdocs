from markdown import markdown

def process_docs(instr):
    outstr = markdown(instr)
    return(outstr)

