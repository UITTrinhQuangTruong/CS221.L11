import argparse
from ParserModel import Parser


def defineArgument():
    '''

        Dinh nghia command line arguments

    '''
    parser = argparse.ArgumentParser()

    # Them input, output
    parser.add_argument("-i", "--Input", help='Input file name')
    parser.add_argument("-o", "--Output", help='Output file name')

    # Nhap input tu ban phim
    parser.add_argument('-n',
                        "--InputFK",
                        action='store_true',
                        help='Input from Keyboard')

    # Them Lexicon, Grammar path
    parser.add_argument("-l", "--Lexicon", help='Path to Lexicon file')
    parser.add_argument("-g", "--Grammar", help='Path to Grammar file')

    # Them flags Tokenizer
    parser.add_argument("-vn",
                        "--TypeTokenizer",
                        action='store_true',
                        help='Tokenizer by VnCoreNLP')

    # Them flags Parser Model
    parser.add_argument("-st",
                        "--ParserModel",
                        action='store_true',
                        help='Parser by StanfordCoreNLP')
    # Them flags Type Output
    parser.add_argument("-x",
                        "--TypeOuput",
                        action='store_true',
                        help='Get 1 or more output')
    return parser


# Dinh nghia command arguments
parser = defineArgument()

# Lay cac Argument
args = parser.parse_args()

# Ham xu ly CKY
Parser(args.InputFK, args.Input, args.Output, args.Lexicon, args.Grammar,
       args.TypeTokenizer, args.ParserModel, args.TypeOuput)
