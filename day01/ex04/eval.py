class Evaluator(object):

    @staticmethod
    def zip_evaluate(coefs, words):
        if len(coefs) != len(words):
            return -1
        return sum([c * len(w) for c, w in zip(coefs, words)])

    @staticmethod
    def enumerate_evaluate(coefs, words):
        if len(coefs) != len(words):
            return -1
        return sum([coefs[i] * len(w) for i, w in enumerate(words)])


if __name__ == "__main__":
    words = ["Le", "lorem", "ipsum", "est", "simple"]
    coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
    print(f"Zip:       {Evaluator.zip_evaluate(coefs, words)}")
    print(f"Enumerate: {Evaluator.enumerate_evaluate(coefs, words)}")
    words = ["Le", "lorem", "ipsum", "n", "est", "pas", "simple"]
    coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
    print(f"Zip Error:       {Evaluator.zip_evaluate(coefs, words)}")
    print(f"Enumerate Error: {Evaluator.zip_evaluate(coefs, words)}")
