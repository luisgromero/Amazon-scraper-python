## Summary
This is a command line application called amazon.py.  The application accepts a couple of flags and an user query, and then prints out the first page of amazon store results based on the user supplied information.

## Example

    ./amazon.py --sort rating --desc office chairs

            Flash Furniture Mid-Back Black Mesh Computer Chair
                Price: $59.88
                    Rating:(22) (242 reviews)
                        Url: http://www.amazon.com/Flash-Furniture-Mid-Back-Black-Computer

                                Boss Black LeatherPlus Executive Chair
                                    Price: $159.99
                                        Rating: (5) (502 reviews)
                                            Url: http://www.amazon.com/Flash-Furniture-Mid-Back-Black-Computer

                                                ... and so on ...

## Notes

1.  The program scrapes the HTML of the following page
    http://www.amazon.com/s/?field-keywords=query
    2.  The program uses other python library(s) e.g(beautiful soup)
    3.  The program allows the user to specify a search query.
    4.  The program accepts the options `--sort {rating, price, name}` and `--{asc, desc}` at a minimum.
