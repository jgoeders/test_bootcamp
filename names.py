from os import fpathconf
import unittest

import pandas


def get_first_last_name(name):
    """Takes a full name as a str and return a typle of (first name, last name)

    >>> get_first_last_name("Jeff Goeders")
    ('Jeff', 'Goeders')

    >>> get_first_last_name("Andrew Lloyd Weber")
    ('Andrew', 'Lloyd Weber')

    >>> get_first_last_name("bruce Wayne")
    ('Bruce', 'Wayne')

    """
    names = name.split(" ")

    # for i in range(len(names)):
    #     names[i] = names[i].capitalize()
    names = [name.capitalize().strip() for name in names]

    # print(names)
    return (names[0], " ".join(names[1:]))


class TestNames(unittest.TestCase):
    def test_some_names(self):
        self.assertEqual(get_first_last_name("bruce wayne"), ("Bruce", "Wayne"))

    def test_multiple_names(self):
        self.assertEqual(get_first_last_name("andrew lloyd weber"), ("Andrew", "Lloyd Weber"))

    def test_golden_file(self):
        df = pandas.read_csv("names.csv")
        df["first_name"] = df.apply(lambda x: get_first_last_name(x["fullname"])[0], axis=1)
        df["last_name"] = df.apply(lambda x: get_first_last_name(x["fullname"])[1], axis=1)

        df.to_csv("out.csv", index=False)

        with open("out.csv") as fp:
            s1 = fp.read()

        with open("golden.csv") as fp:
            s2 = fp.read()
        self.assertEqual(s1, s2)
