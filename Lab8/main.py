import multiprocessing

def second_pipeline(pipeline_in, pipeline_out):
    text = pipeline_in.recv()
    
    processed_text = text.upper()
    pipeline_out.send(processed_text)
    
    pipeline_in.close()
    pipeline_out.close()

def third_pipeline(pipeline_in):
    final_text = pipeline_in.recv()
    
    print(final_text)
    
    pipeline_in.close()

def runPipeline():
    p1_read, p1_write = multiprocessing.Pipe(duplex=False)
    p2_read, p2_write = multiprocessing.Pipe(duplex=False)

    p2 = multiprocessing.Process(target=second_pipeline, args=(p1_read, p2_write))
    p3 = multiprocessing.Process(target=third_pipeline, args=(p2_read,))

    p2.start()
    p3.start()

    print("Type a message")
    message = input()
    
    p1_write.send(message)
    p1_write.close()
    print("Text sent to the pipeline, waiting for a result...\n")

    p2.join()
    p3.join()

if __name__ == '__main__':
    runPipeline()