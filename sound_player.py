#!python3
import ui, sound, os, base64, threading, time, sys
UIs = base64.b64decode('WwogIHsKICAgICJub2RlcyIgOiBbCiAgICAgIHsKICAgICAgICAibm9kZXMiIDogWwoKICAgICAgICBdLAogICAgICAgICJmcmFtZSIgOiAie3sxNTEsIDM5OH0sIHsyMTAsIDkyfX0iLAogICAgICAgICJjbGFzcyIgOiAiVGFibGVWaWV3IiwKICAgICAgICAiYXR0cmlidXRlcyIgOiB7CiAgICAgICAgICAidXVpZCIgOiAiMTBEQjVDMUYtQ0JBOC00NjI3LTkxRDMtOTdGMTQ3OTM2RDhBIiwKICAgICAgICAgICJkYXRhX3NvdXJjZV9hY3Rpb24iIDogIlNlbGVjdG9yIiwKICAgICAgICAgICJiYWNrZ3JvdW5kX2NvbG9yIiA6ICJSR0JBKDAuMTQwMTE4LDAuMTQwMTE4LDAuMTQwMTE4LDEuMDAwMDAwKSIsCiAgICAgICAgICAiZnJhbWUiIDogInt7NTYsIDE4NX0sIHsyMDAsIDIwMH19IiwKICAgICAgICAgICJkYXRhX3NvdXJjZV9pdGVtcyIgOiAiMeODiOODqeODg+OCr+OBruOBv+ODquODlOODvOODiFxu44Oq44OU44O844OI44KS44Kq44OV44Gr44GZ44KLIiwKICAgICAgICAgICJ0aW50X2NvbG9yIiA6ICJSR0JBKDEuMDAwMDAwLDAuMDMxMjUwLDAuMDMxMjUwLDEuMDAwMDAwKSIsCiAgICAgICAgICAiZGF0YV9zb3VyY2VfbnVtYmVyX29mX2xpbmVzIiA6IDEsCiAgICAgICAgICAiZGF0YV9zb3VyY2VfZGVsZXRlX2VuYWJsZWQiIDogZmFsc2UsCiAgICAgICAgICAiZGF0YV9zb3VyY2VfZm9udF9zaXplIiA6IDE4LAogICAgICAgICAgInJvd19oZWlnaHQiIDogNDQsCiAgICAgICAgICAiY2xhc3MiIDogIlRhYmxlVmlldyIsCiAgICAgICAgICAibmFtZSIgOiAiTW9kZV9TZWxlY3QiLAogICAgICAgICAgImZsZXgiIDogIldITFJUQiIKICAgICAgICB9LAogICAgICAgICJzZWxlY3RlZCIgOiBmYWxzZQogICAgICB9LAogICAgICB7CiAgICAgICAgIm5vZGVzIiA6IFsKCiAgICAgICAgXSwKICAgICAgICAiZnJhbWUiIDogInt7NzYsIDUzNX0sIHs4MCwgODJ9fSIsCiAgICAgICAgImNsYXNzIiA6ICJCdXR0b24iLAogICAgICAgICJhdHRyaWJ1dGVzIiA6IHsKICAgICAgICAgICJ1dWlkIiA6ICJENjFDMDE4My1EMjZELTQ4NEQtOTZFNS03NjdEN0UyMDExREQiLAogICAgICAgICAgImltYWdlX25hbWUiIDogImlvYjpzdG9wXzI1NiIsCiAgICAgICAgICAiZm9udF9zaXplIiA6IDE1LAogICAgICAgICAgImNvcm5lcl9yYWRpdXMiIDogMSwKICAgICAgICAgICJmcmFtZSIgOiAie3sxMTYsIDI2OX0sIHs4MCwgMzJ9fSIsCiAgICAgICAgICAiYm9yZGVyX2NvbG9yIiA6ICJSR0JBKDAuMDMyMDE5LDAuMDMyMDE5LDAuMDMyMDE5LDEuMDAwMDAwKSIsCiAgICAgICAgICAiYm9yZGVyX3dpZHRoIiA6IDEsCiAgICAgICAgICAidGl0bGUiIDogIkJ1dHRvbiIsCiAgICAgICAgICAiYWN0aW9uIiA6ICJTdG9wIiwKICAgICAgICAgICJjbGFzcyIgOiAiQnV0dG9uIiwKICAgICAgICAgICJuYW1lIiA6ICJTdG9wIiwKICAgICAgICAgICJmbGV4IiA6ICJXSExSVEIiCiAgICAgICAgfSwKICAgICAgICAic2VsZWN0ZWQiIDogZmFsc2UKICAgICAgfSwKICAgICAgewogICAgICAgICJub2RlcyIgOiBbCgogICAgICAgIF0sCiAgICAgICAgImZyYW1lIiA6ICJ7ezIwNiwgNTM1fSwgezgwLCA4Mn19IiwKICAgICAgICAiY2xhc3MiIDogIkJ1dHRvbiIsCiAgICAgICAgImF0dHJpYnV0ZXMiIDogewogICAgICAgICAgInV1aWQiIDogIkQ2MUMwMTgzLUQyNkQtNDg0RC05NkU1LTc2N0Q3RTIwMTFERCIsCiAgICAgICAgICAibmFtZSIgOiAiUGxheSIsCiAgICAgICAgICAiZm9udF9zaXplIiA6IDE1LAogICAgICAgICAgImNvcm5lcl9yYWRpdXMiIDogMSwKICAgICAgICAgICJmcmFtZSIgOiAie3sxMTYsIDI2OX0sIHs4MCwgMzJ9fSIsCiAgICAgICAgICAiYm9yZGVyX2NvbG9yIiA6ICJSR0JBKDAuMDMzMjIwLDAuMDMzMjIwLDAuMDMzMjIwLDEuMDAwMDAwKSIsCiAgICAgICAgICAiYm9yZGVyX3dpZHRoIiA6IDEsCiAgICAgICAgICAidGl0bGUiIDogIlBsYXkiLAogICAgICAgICAgImFjdGlvbiIgOiAiUGxheSIsCiAgICAgICAgICAiY2xhc3MiIDogIkJ1dHRvbiIsCiAgICAgICAgICAiaW1hZ2VfbmFtZSIgOiAiaW9iOnBsYXlfMjU2IiwKICAgICAgICAgICJmbGV4IiA6ICJXSExSVEIiCiAgICAgICAgfSwKICAgICAgICAic2VsZWN0ZWQiIDogdHJ1ZQogICAgICB9LAogICAgICB7CiAgICAgICAgIm5vZGVzIiA6IFsKCiAgICAgICAgXSwKICAgICAgICAiZnJhbWUiIDogInt7NiwgNzB9LCB7MzU1LCA0MH19IiwKICAgICAgICAiY2xhc3MiIDogIkxhYmVsIiwKICAgICAgICAiYXR0cmlidXRlcyIgOiB7CiAgICAgICAgICAidXVpZCIgOiAiQjk2RDZDNkYtNTZERi00OTE1LTkxREMtMzAyQThFREE5OUFEIiwKICAgICAgICAgICJmbGV4IiA6ICJXSExSVEIiLAogICAgICAgICAgImNvcm5lcl9yYWRpdXMiIDogMSwKICAgICAgICAgICJiYWNrZ3JvdW5kX2NvbG9yIiA6ICJSR0JBKDAuMTM4OTE3LDAuMTM4OTE3LDAuMTM4OTE3LDEuMDAwMDAwKSIsCiAgICAgICAgICAiZnJhbWUiIDogInt7MTA5LCAzMDJ9LCB7MTUwLCAzMn19IiwKICAgICAgICAgICJib3JkZXJfY29sb3IiIDogIlJHQkEoMC4wMzMyMjAsMC4wMzMyMjAsMC4wMzMyMjAsMS4wMDAwMDApIiwKICAgICAgICAgICJib3JkZXJfd2lkdGgiIDogMSwKICAgICAgICAgICJhbGlnbm1lbnQiIDogImNlbnRlciIsCiAgICAgICAgICAidGV4dF9jb2xvciIgOiAiUkdCQSgxLjAwMDAwMCwwLjAzMTI1MCwwLjAzMTI1MCwxLjAwMDAwMCkiLAogICAgICAgICAgInRleHQiIDogIuODleOCqeODq+ODgOWGhToiLAogICAgICAgICAgImZvbnRfbmFtZSIgOiAiPFN5c3RlbT4iLAogICAgICAgICAgImNsYXNzIiA6ICJMYWJlbCIsCiAgICAgICAgICAibmFtZSIgOiAiIiwKICAgICAgICAgICJmb250X3NpemUiIDogMTgKICAgICAgICB9LAogICAgICAgICJzZWxlY3RlZCIgOiBmYWxzZQogICAgICB9LAogICAgICB7CiAgICAgICAgIm5vZGVzIiA6IFsKCiAgICAgICAgXSwKICAgICAgICAiZnJhbWUiIDogInt7NiwgMjh9LCB7ODEsIDQwfX0iLAogICAgICAgICJjbGFzcyIgOiAiTGFiZWwiLAogICAgICAgICJhdHRyaWJ1dGVzIiA6IHsKICAgICAgICAgICJuYW1lIiA6ICIiLAogICAgICAgICAgInRleHRfY29sb3IiIDogIlJHQkEoMS4wMDAwMDAsMC4wMDAwMDAsMC4wMDAwMDAsMS4wMDAwMDApIiwKICAgICAgICAgICJmbGV4IiA6ICJXSExSVEIiLAogICAgICAgICAgImZyYW1lIiA6ICJ7ezEwOSwgMzAyfSwgezE1MCwgMzJ9fSIsCiAgICAgICAgICAidXVpZCIgOiAiMkRDQUNGMEMtOTgyNS00NkI1LUIyRUItRjMwOUEzMjZGQzU1IiwKICAgICAgICAgICJjbGFzcyIgOiAiTGFiZWwiLAogICAgICAgICAgImFsaWdubWVudCIgOiAiY2VudGVyIiwKICAgICAgICAgICJ0ZXh0IiA6ICLjg5Hjgrk6IiwKICAgICAgICAgICJmb250X3NpemUiIDogMTgsCiAgICAgICAgICAiZm9udF9uYW1lIiA6ICI8U3lzdGVtLUJvbGQ+IgogICAgICAgIH0sCiAgICAgICAgInNlbGVjdGVkIiA6IGZhbHNlCiAgICAgIH0sCiAgICAgIHsKICAgICAgICAibm9kZXMiIDogWwoKICAgICAgICBdLAogICAgICAgICJmcmFtZSIgOiAie3s3NiwgNDk4fSwgezgwLCAzMn19IiwKICAgICAgICAiY2xhc3MiIDogIkxhYmVsIiwKICAgICAgICAiYXR0cmlidXRlcyIgOiB7CiAgICAgICAgICAidXVpZCIgOiAiNTY2OTkyQjEtQjBBQy00NUU0LUIxRDUtQTI2M0Q2M0ZFMjhEIiwKICAgICAgICAgICJmb250X3NpemUiIDogMTgsCiAgICAgICAgICAiY29ybmVyX3JhZGl1cyIgOiAxLAogICAgICAgICAgImZyYW1lIiA6ICJ7ezEwOSwgMzEzfSwgezE1MCwgMzJ9fSIsCiAgICAgICAgICAiYm9yZGVyX2NvbG9yIiA6ICJSR0JBKDAuMDMyMDE5LDAuMDMyMDE5LDAuMDMyMDE5LDEuMDAwMDAwKSIsCiAgICAgICAgICAiYm9yZGVyX3dpZHRoIiA6IDEsCiAgICAgICAgICAiYWxpZ25tZW50IiA6ICJjZW50ZXIiLAogICAgICAgICAgInRleHRfY29sb3IiIDogIlJHQkEoMS4wMDAwMDAsMC4wMDAwMDAsMC4wMDAwMDAsMS4wMDAwMDApIiwKICAgICAgICAgICJ0ZXh0IiA6ICLlgZzmraIiLAogICAgICAgICAgImZvbnRfbmFtZSIgOiAiPFN5c3RlbT4iLAogICAgICAgICAgImNsYXNzIiA6ICJMYWJlbCIsCiAgICAgICAgICAibmFtZSIgOiAiIiwKICAgICAgICAgICJmbGV4IiA6ICJXSExSVEIiCiAgICAgICAgfSwKICAgICAgICAic2VsZWN0ZWQiIDogZmFsc2UKICAgICAgfSwKICAgICAgewogICAgICAgICJub2RlcyIgOiBbCgogICAgICAgIF0sCiAgICAgICAgImZyYW1lIiA6ICJ7ezIwNiwgNDk4fSwgezgwLCAzMn19IiwKICAgICAgICAiY2xhc3MiIDogIkxhYmVsIiwKICAgICAgICAiYXR0cmlidXRlcyIgOiB7CiAgICAgICAgICAidXVpZCIgOiAiNTY2OTkyQjEtQjBBQy00NUU0LUIxRDUtQTI2M0Q2M0ZFMjhEIiwKICAgICAgICAgICJmb250X3NpemUiIDogMTgsCiAgICAgICAgICAiY29ybmVyX3JhZGl1cyIgOiAxLAogICAgICAgICAgImZyYW1lIiA6ICJ7ezEwOSwgMzEzfSwgezE1MCwgMzJ9fSIsCiAgICAgICAgICAiYm9yZGVyX2NvbG9yIiA6ICJSR0JBKDAuMDMzMjIwLDAuMDMzMjIwLDAuMDMzMjIwLDEuMDAwMDAwKSIsCiAgICAgICAgICAiYm9yZGVyX3dpZHRoIiA6IDEsCiAgICAgICAgICAiYWxpZ25tZW50IiA6ICJjZW50ZXIiLAogICAgICAgICAgInRleHQiIDogIuWGjeeUnyIsCiAgICAgICAgICAidGV4dF9jb2xvciIgOiAiUkdCQSgxLjAwMDAwMCwwLjAwMDAwMCwwLjAwMDAwMCwxLjAwMDAwMCkiLAogICAgICAgICAgImZvbnRfbmFtZSIgOiAiPFN5c3RlbT4iLAogICAgICAgICAgImNsYXNzIiA6ICJMYWJlbCIsCiAgICAgICAgICAibmFtZSIgOiAiIiwKICAgICAgICAgICJmbGV4IiA6ICJXSExSVEIiCiAgICAgICAgfSwKICAgICAgICAic2VsZWN0ZWQiIDogZmFsc2UKICAgICAgfSwKICAgICAgewogICAgICAgICJub2RlcyIgOiBbCgogICAgICAgIF0sCiAgICAgICAgImZyYW1lIiA6ICJ7ezYsIDExMX0sIHszNTUsIDI1M319IiwKICAgICAgICAiY2xhc3MiIDogIlRhYmxlVmlldyIsCiAgICAgICAgImF0dHJpYnV0ZXMiIDogewogICAgICAgICAgInV1aWQiIDogIjg3QzEwQTI0LTMxQTQtNDkxNi04RDg0LTlDOTdDOUVFNzQxQSIsCiAgICAgICAgICAiZGF0YV9zb3VyY2VfYWN0aW9uIiA6ICJGaWxlTmFtZSIsCiAgICAgICAgICAiYmFja2dyb3VuZF9jb2xvciIgOiAiUkdCQSgwLjE0MTE3NiwwLjE0MTE3NiwwLjE0MTE3NiwxLjAwMDAwMCkiLAogICAgICAgICAgImZyYW1lIiA6ICJ7ezg0LCAyMjl9LCB7MjAwLCAyMDB9fSIsCiAgICAgICAgICAiZGF0YV9zb3VyY2VfaXRlbXMiIDogIiIsCiAgICAgICAgICAiZGF0YV9zb3VyY2VfbnVtYmVyX29mX2xpbmVzIiA6IDEsCiAgICAgICAgICAiZGF0YV9zb3VyY2VfZGVsZXRlX2VuYWJsZWQiIDogZmFsc2UsCiAgICAgICAgICAiZGF0YV9zb3VyY2VfZm9udF9zaXplIiA6IDE4LAogICAgICAgICAgInJvd19oZWlnaHQiIDogNDQsCiAgICAgICAgICAiY2xhc3MiIDogIlRhYmxlVmlldyIsCiAgICAgICAgICAibmFtZSIgOiAiTGlzdEZvbGRlcnMiLAogICAgICAgICAgImZsZXgiIDogIldITFJUQiIKICAgICAgICB9LAogICAgICAgICJzZWxlY3RlZCIgOiBmYWxzZQogICAgICB9LAogICAgICB7CiAgICAgICAgIm5vZGVzIiA6IFsKCiAgICAgICAgXSwKICAgICAgICAiZnJhbWUiIDogInt7NiwgMzk4fSwgezE1MCwgOTJ9fSIsCiAgICAgICAgImNsYXNzIiA6ICJUYWJsZVZpZXciLAogICAgICAgICJhdHRyaWJ1dGVzIiA6IHsKICAgICAgICAgICJ1dWlkIiA6ICI5NDcyRTMwNi1BNTU1LTQzQ0ItQUI4Qy01OTVGRUQ2ODAxMUUiLAogICAgICAgICAgImRhdGFfc291cmNlX2FjdGlvbiIgOiAiVGhyZWVEU291bmRNb2RlIiwKICAgICAgICAgICJiYWNrZ3JvdW5kX2NvbG9yIiA6ICJSR0JBKDAuMTQxMTc2LDAuMTQxMTc2LDAuMTQxMTc2LDEuMDAwMDAwKSIsCiAgICAgICAgICAiZnJhbWUiIDogInt7ODQsIDIyOX0sIHsyMDAsIDIwMH19IiwKICAgICAgICAgICJkYXRhX3NvdXJjZV9pdGVtcyIgOiAi56uL5L2T6Z+z6Z+/44KS44Kq44Oz44Gr44GZ44KLXG7nq4vkvZPpn7Ppn7/jgpLjgqrjg5XjgavjgZnjgosiLAogICAgICAgICAgImRhdGFfc291cmNlX251bWJlcl9vZl9saW5lcyIgOiAxLAogICAgICAgICAgInRpbnRfY29sb3IiIDogIlJHQkEoMS4wMDAwMDAsMC4wMzEzNzMsMC4wMzEzNzMsMS4wMDAwMDApIiwKICAgICAgICAgICJkYXRhX3NvdXJjZV9kZWxldGVfZW5hYmxlZCIgOiBmYWxzZSwKICAgICAgICAgICJkYXRhX3NvdXJjZV9mb250X3NpemUiIDogMTIsCiAgICAgICAgICAicm93X2hlaWdodCIgOiA0NCwKICAgICAgICAgICJjbGFzcyIgOiAiVGFibGVWaWV3IiwKICAgICAgICAgICJuYW1lIiA6ICIzRFNvdW5kIiwKICAgICAgICAgICJmbGV4IiA6ICJXSExSVEIiCiAgICAgICAgfSwKICAgICAgICAic2VsZWN0ZWQiIDogZmFsc2UKICAgICAgfSwKICAgICAgewogICAgICAgICJub2RlcyIgOiBbCgogICAgICAgIF0sCiAgICAgICAgImZyYW1lIiA6ICJ7ezYsIDM2M30sIHszNTUsIDM0fX0iLAogICAgICAgICJjbGFzcyIgOiAiU2xpZGVyIiwKICAgICAgICAiYXR0cmlidXRlcyIgOiB7CiAgICAgICAgICAiYWN0aW9uIiA6ICIiLAogICAgICAgICAgImZsZXgiIDogIldITFJUQiIsCiAgICAgICAgICAiY29udGludW91cyIgOiB0cnVlLAogICAgICAgICAgImZyYW1lIiA6ICJ7ezg0LCAzMTJ9LCB7MjAwLCAzNH19IiwKICAgICAgICAgICJ0aW50X2NvbG9yIiA6ICJSR0JBKDEuMDAwMDAwLDAuMDMxMzczLDAuMDMxMzczLDEuMDAwMDAwKSIsCiAgICAgICAgICAidXVpZCIgOiAiMDUzOEI0MUQtMkQ0NS00NDg0LTgyQzQtNTVBMTE4RURFQjQ3IiwKICAgICAgICAgICJjbGFzcyIgOiAiU2xpZGVyIiwKICAgICAgICAgICJ2YWx1ZSIgOiAwLAogICAgICAgICAgImJhY2tncm91bmRfY29sb3IiIDogIlJHQkEoMC4xMzcyNTUsMC4xMzcyNTUsMC4xMzcyNTUsMS4wMDAwMDApIiwKICAgICAgICAgICJuYW1lIiA6ICJTZWVrQmFyIgogICAgICAgIH0sCiAgICAgICAgInNlbGVjdGVkIiA6IGZhbHNlCiAgICAgIH0sCiAgICAgIHsKICAgICAgICAibm9kZXMiIDogWwoKICAgICAgICBdLAogICAgICAgICJmcmFtZSIgOiAie3s3NiwgMjh9LCB7Mjg1LCA0MH19IiwKICAgICAgICAiY2xhc3MiIDogIkxhYmVsIiwKICAgICAgICAiYXR0cmlidXRlcyIgOiB7CiAgICAgICAgICAidXVpZCIgOiAiOUFDQzQ4MjgtRjZENS00RjJDLUExREEtMzdFQTkxMTE3ODg0IiwKICAgICAgICAgICJmb250X3NpemUiIDogMTcsCiAgICAgICAgICAiYmFja2dyb3VuZF9jb2xvciIgOiAiUkdCQSgwLjE0MTE3NiwwLjE0MTE3NiwwLjE0MTE3NiwxLjAwMDAwMCkiLAogICAgICAgICAgImZyYW1lIiA6ICJ7ezEwOSwgMzEzfSwgezE1MCwgMzJ9fSIsCiAgICAgICAgICAidGludF9jb2xvciIgOiAiUkdCQSgxLjAwMDAwMCwwLjAzMTM3MywwLjAzMTM3MywxLjAwMDAwMCkiLAogICAgICAgICAgImFsaWdubWVudCIgOiAibGVmdCIsCiAgICAgICAgICAidGV4dF9jb2xvciIgOiAiUkdCQSgxLjAwMDAwMCwwLjAzMTM3MywwLjAzMTM3MywxLjAwMDAwMCkiLAogICAgICAgICAgInRleHQiIDogIiIsCiAgICAgICAgICAiZm9udF9uYW1lIiA6ICI8U3lzdGVtPiIsCiAgICAgICAgICAiY2xhc3MiIDogIkxhYmVsIiwKICAgICAgICAgICJuYW1lIiA6ICJMaWJyYXJ5X1BhdGgiLAogICAgICAgICAgImZsZXgiIDogIldITFJUQiIKICAgICAgICB9LAogICAgICAgICJzZWxlY3RlZCIgOiBmYWxzZQogICAgICB9CiAgICBdLAogICAgImZyYW1lIiA6ICJ7ezAsIDB9LCB7MzY3LCA2NTh9fSIsCiAgICAiY2xhc3MiIDogIlZpZXciLAogICAgImF0dHJpYnV0ZXMiIDogewogICAgICAiZmxleCIgOiAiIiwKICAgICAgImN1c3RvbV9jbGFzcyIgOiAiU291bmRQbGF5ZXIiLAogICAgICAidGludF9jb2xvciIgOiAiUkdCQSgxLjAwMDAwMCwwLjAzMTI1MCwwLjAzMTI1MCwxLjAwMDAwMCkiLAogICAgICAiZW5hYmxlZCIgOiB0cnVlLAogICAgICAiYm9yZGVyX2NvbG9yIiA6ICJSR0JBKDAuMDAwMDAwLDAuMDAwMDAwLDAuMDAwMDAwLDEuMDAwMDAwKSIsCiAgICAgICJiYWNrZ3JvdW5kX2NvbG9yIiA6ICJSR0JBKDAuMTAxNjgzLDAuMTAxNjgzLDAuMTAxNjgzLDEuMDAwMDAwKSIsCiAgICAgICJuYW1lIiA6ICJTb3VuZCBQbGF5ZXIiCiAgICB9LAogICAgInNlbGVjdGVkIiA6IGZhbHNlCiAgfQpd').decode()

Mode = ''
SoundMode = ''
NowClosed = ['0']
PlayMusicList = []
MDirName = []
LDirs = []
LFiles = []

def __init__():
    os.makedirs(os.path.join(os.environ['HOME'], 'Documents', 'AudioFiles'), exist_ok=True)

def ListView(ListsView):
    global Path, MDirName
    try:
        if ListsView['ListFolders'].data_source.items[0] == '':
            del ListsView['ListFolders'].data_source.items[0]
    except:
        pass
    if not ''.join(ListsView['ListFolders'].data_source.items) == '':
        try:
            Pl = [0]
            for U in Pl:
                for L in range(len(ListsView['ListFolders'].data_source.items)):
                    try:
                        del ListsView['ListFolders'].data_source.items[L]
                    except:
                        Pl.append(U+1)
                if ''.join(ListsView['ListFolders'].data_source.items) == '':
                    break
        except:
            pass
    try:
        Path = '.'
        RawFiles = sorted(os.listdir(Path))
        for Files in RawFiles:
            if os.path.isfile(Files):
                LFiles.append(Files)
            elif os.path.islink(Files):
                LDirs.append('[{}]'.format(Files))
            elif os.path.isdir(Files):
                LDirs.append('[{}]'.format(Files))
            else:
                LFiles.append(Files)
        Musics = []
        for MFile in MusicFileFinder(Path):
            if os.path.isfile(MFile):
                Musics.append(MFile)
        MusicFiles = []
        for MF in range(len(sorted(Musics))):
            MDirName.append(str(sorted(Musics)[MF].split(sorted(Musics)[MF].split('/')[-1])[0]))
            MusicFiles.append(str(sorted(Musics)[MF].split('/')[-1]))
        ListsView['ListFolders'].data_source.items = MusicFiles
    except Exception as W:
        print(W)
        pass

def MusicFileFinder(Dir):
    for root, _, f, in os.walk(Dir):
        yield root
        for File in f:
            if File.split('.')[-1].lower() == 'mp3':
                yield os.path.join(root, File)
            if File.split('.')[-1].lower() == 'm4a':
                yield os.path.join(root, File)
            if File.split('.')[-1].lower() == 'flac':
                yield os.path.join(root, File)
            if File.split('.')[-1].lower() == 'wav':
                yield os.path.join(root, File)

def Selector(s):
    global Mode
    try:
        selected = s.items[s.selected_row]
        if selected == '1トラックのみリピート':
            Mode = True
        elif selected == 'リピートをオフにする':
            Mode = False
    except:
        pass

def FileName(File):
    global FileNames, FileIndex
    try:
        FileIndex = File.selected_row
        FileNames = File.items[FileIndex]
    except:
        FileNames = ''

def ThreeDSoundMode(Moder):
    global SoundMode
    try:
        SoundMode = Moder.items[Moder.selected_row]
    except Exception as E:
        print(E)
        SoundMode = '立体音響をオフにする'

def Play(_):
    global PlayMusicList
    try:
        if Mode == '':
            Modes = False
        else:
            Modes = Mode
        if SoundMode == '立体音響をオンにする':
            FilePath = os.path.join(MDirName[FileIndex], FileNames)
            PlayMusicList = [sound.Player('{}'.format(FilePath)) for _ in range(2)]
            for Play in PlayMusicList:
                if Modes:
                    Play.play()
                    Play.number_of_loops = -1
                    time.sleep(0.023)
                else:
                    Play.play()
                    time.sleep(0.023)
        elif SoundMode == '立体音響をオフにする':
            FilePath = os.path.join(MDirName[FileIndex], FileNames)
            PlayMusicList = [sound.Player('{}'.format(FilePath)) for _ in range(1)]
            for Play in PlayMusicList:
                if Modes:
                    Play.play()
                    Play.number_of_loops = -1
                else:
                    Play.play()
        else:
            FilePath = os.path.join(MDirName[FileIndex], FileNames)
            PlayMusicList = [sound.Player('{}'.format(FilePath)) for _ in range(1)]
            for Play in PlayMusicList:
                if Modes:
                    Play.play()
                    Play.number_of_loops = -1
                else:
                    Play.play()
    except Exception as E:
        print(E)
        pass

def Stop(_):
    try:
        for Play in PlayMusicList:
            Play.stop()
    except:
        pass

class SoundPlayer(ui.View):
    def will_close(self):
        try:
            for Play in PlayMusicList:
                Play.stop()
            NowClosed[0] = '1'
            sys.exit(0)
        except:
            pass

class SeekBar(threading.Thread):
    def __init__(self, _ui):
        threading.Thread.__init__(self)
        self._ui = _ui

    def run(self):
        while True:
            try:
                if NowClosed[0] == '0':
                    for Play in PlayMusicList:
                        try:
                            self._ui['SeekBar'].value = int(str(Play.current_time).split('.')[0]) /  int(str(Play.duration).split('.')[0])
                        except:
                            pass
                else:
                    Stop('0')
                    quit()
                    break
            except KeyboardInterrupt:
                Stop('0')
                quit()
                break

def main():
    __init__()
    RootDirectoryPath = os.path.join(os.environ['HOME'], 'Documents', 'AudioFiles')
    os.chdir(RootDirectoryPath)
    soundP = ui.load_view_str(UIs)
    soundP['Library_Path'].text = RootDirectoryPath.replace(os.environ['HOME'], '~')
    ListView(soundP)
    SeekBar(soundP).start()
    soundP.present('panel')

if __name__ == '__main__':
    main()