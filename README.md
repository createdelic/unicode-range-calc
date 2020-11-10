# unicode-range-calc

Calculates what ranges of Unicode characters are used in a set of files.

Created to find out what Unicode ranges to use when creating a Font Asset for TextMesh Pro.

## Usage Example

```
$ python3 unicode-range-calc.py examples/lorem_latin.txt examples/lorem_cyrillic.txt
002c     
002e     
0045     
0048     
004c     
0051     
0061-0065
0068-0069
006c-0076
0414-0415
0418     
041b     
0430-0435
0438     
043b-0446
044f

$ python3 unicode-range-calc.py --show-chars examples/lorem_latin.txt examples/lorem_cyrillic.txt
002c(,)        
002e(.)        
0045(E)        
0048(H)        
004c(L)        
0051(Q)        
0061(a)-0065(e)
0068(h)-0069(i)
006c(l)-0076(v)
0414(Д)-0415(Е)
0418(И)        
041b(Л)        
0430(а)-0435(е)
0438(и)        
043b(л)-0446(ц)
044f(я)              

$ python3 unicode-range-calc.py --show-chars --ignore-chars ".," examples/lorem_latin.txt examples/lorem_cyrillic.txt
0045(E)        
0048(H)        
004c(L)        
0051(Q)        
0061(a)-0065(e)
0068(h)-0069(i)
006c(l)-0076(v)
0414(Д)-0415(Е)
0418(И)        
041b(Л)        
0430(а)-0435(е)
0438(и)        
043b(л)-0446(ц)
044f(я)                                                                                                                                                                                                                                                                       
```