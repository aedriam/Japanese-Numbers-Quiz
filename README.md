# Japanese-Numbers-Quiz
Programmed by Matthew Unrue for his Japanese students.<br/>
Version 0.3<br/>
9/18/2017 & 9/21/2017

A CLI quiz on the pronunciation and writing of numbers between 0 and 99,999,999 in Japanese.

Determines the kanji or kana representation of numbers by recursively calling the get_pronunciation() and get_kanji() functions while chunking numbers into the Japanese language's [myriad](https://en.wikipedia.org/wiki/Myriad) grouping system of 10,000s in order to properly determine which dictionary lookups to use for each numeral.

The pronunciations used are primarily [on'yomi](https://en.wikipedia.org/wiki/Kanji#On'yomi_(Sino-Japanese_reading)), but よん and なな are used from the [kun'yomi](https://en.wikipedia.org/wiki/Kanji#Kun'yomi_(native_reading)), as these are the typical  pronunciations for numbers while simply counting according to the [Genki textbook](http://genki.japantimes.co.jp/index_en) on pages 46 & 47 in the Expression Notes 2 section.

A further discussion on the Japanese stack exchange exists [here.](https://japanese.stackexchange.com/questions/328/how-to-choose-between-%E3%82%88%E3%82%93-yon-vs-%E3%81%97-shi-for-%E5%9B%9B-4-and-%E3%81%97%E3%81%A1-shichi-vs)
