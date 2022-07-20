import ui, sound, os, base64, time, sys
UIs = base64.b64decode('WwogIHsKICAgICJub2RlcyIgOiBbCiAgICAgIHsKICAgICAgICAibm9kZXMiIDogWwoKICAgICAgICBdLAogICAgICAgICJmcmFtZSIgOiAie3sxNTEsIDM5OH0sIHsyMTAsIDkyfX0iLAogICAgICAgICJjbGFzcyIgOiAiVGFibGVWaWV3IiwKICAgICAgICAiYXR0cmlidXRlcyIgOiB7CiAgICAgICAgICAidXVpZCIgOiAiMTBEQjVDMUYtQ0JBOC00NjI3LTkxRDMtOTdGMTQ3OTM2RDhBIiwKICAgICAgICAgICJkYXRhX3NvdXJjZV9hY3Rpb24iIDogIlNlbGVjdG9yIiwKICAgICAgICAgICJiYWNrZ3JvdW5kX2NvbG9yIiA6ICJSR0JBKDAuMTQwMTE4LDAuMTQwMTE4LDAuMTQwMTE4LDEuMDAwMDAwKSIsCiAgICAgICAgICAiZnJhbWUiIDogInt7NTYsIDE4NX0sIHsyMDAsIDIwMH19IiwKICAgICAgICAgICJkYXRhX3NvdXJjZV9pdGVtcyIgOiAiMeODiOODqeODg+OCr+OBruOBv+ODquODlOODvOODiFxu44Oq44OU44O844OI44KS44Kq44OV44Gr44GZ44KLIiwKICAgICAgICAgICJ0aW50X2NvbG9yIiA6ICJSR0JBKDEuMDAwMDAwLDAuMDMxMjUwLDAuMDMxMjUwLDEuMDAwMDAwKSIsCiAgICAgICAgICAiZGF0YV9zb3VyY2VfbnVtYmVyX29mX2xpbmVzIiA6IDEsCiAgICAgICAgICAiZGF0YV9zb3VyY2VfZGVsZXRlX2VuYWJsZWQiIDogZmFsc2UsCiAgICAgICAgICAiZGF0YV9zb3VyY2VfZm9udF9zaXplIiA6IDE4LAogICAgICAgICAgInJvd19oZWlnaHQiIDogNDQsCiAgICAgICAgICAiY2xhc3MiIDogIlRhYmxlVmlldyIsCiAgICAgICAgICAibmFtZSIgOiAiTW9kZV9TZWxlY3QiLAogICAgICAgICAgImZsZXgiIDogIkxSVEIiCiAgICAgICAgfSwKICAgICAgICAic2VsZWN0ZWQiIDogZmFsc2UKICAgICAgfSwKICAgICAgewogICAgICAgICJub2RlcyIgOiBbCgogICAgICAgIF0sCiAgICAgICAgImZyYW1lIiA6ICJ7ezc2LCA1MzV9LCB7ODAsIDgyfX0iLAogICAgICAgICJjbGFzcyIgOiAiQnV0dG9uIiwKICAgICAgICAiYXR0cmlidXRlcyIgOiB7CiAgICAgICAgICAidXVpZCIgOiAiRDYxQzAxODMtRDI2RC00ODRELTk2RTUtNzY3RDdFMjAxMUREIiwKICAgICAgICAgICJpbWFnZV9uYW1lIiA6ICJpb2I6c3RvcF8yNTYiLAogICAgICAgICAgImZvbnRfc2l6ZSIgOiAxNSwKICAgICAgICAgICJjb3JuZXJfcmFkaXVzIiA6IDEsCiAgICAgICAgICAiZnJhbWUiIDogInt7MTE2LCAyNjl9LCB7ODAsIDMyfX0iLAogICAgICAgICAgImJvcmRlcl9jb2xvciIgOiAiUkdCQSgwLjAzMjAxOSwwLjAzMjAxOSwwLjAzMjAxOSwxLjAwMDAwMCkiLAogICAgICAgICAgImJvcmRlcl93aWR0aCIgOiAxLAogICAgICAgICAgInRpdGxlIiA6ICJCdXR0b24iLAogICAgICAgICAgImFjdGlvbiIgOiAiU3RvcCIsCiAgICAgICAgICAiY2xhc3MiIDogIkJ1dHRvbiIsCiAgICAgICAgICAibmFtZSIgOiAiU3RvcCIsCiAgICAgICAgICAiZmxleCIgOiAiTFJUQiIKICAgICAgICB9LAogICAgICAgICJzZWxlY3RlZCIgOiBmYWxzZQogICAgICB9LAogICAgICB7CiAgICAgICAgIm5vZGVzIiA6IFsKCiAgICAgICAgXSwKICAgICAgICAiZnJhbWUiIDogInt7MjA2LCA1MzV9LCB7ODAsIDgyfX0iLAogICAgICAgICJjbGFzcyIgOiAiQnV0dG9uIiwKICAgICAgICAiYXR0cmlidXRlcyIgOiB7CiAgICAgICAgICAidXVpZCIgOiAiRDYxQzAxODMtRDI2RC00ODRELTk2RTUtNzY3RDdFMjAxMUREIiwKICAgICAgICAgICJuYW1lIiA6ICJQbGF5IiwKICAgICAgICAgICJmb250X3NpemUiIDogMTUsCiAgICAgICAgICAiY29ybmVyX3JhZGl1cyIgOiAxLAogICAgICAgICAgImZyYW1lIiA6ICJ7ezExNiwgMjY5fSwgezgwLCAzMn19IiwKICAgICAgICAgICJib3JkZXJfY29sb3IiIDogIlJHQkEoMC4wMzMyMjAsMC4wMzMyMjAsMC4wMzMyMjAsMS4wMDAwMDApIiwKICAgICAgICAgICJib3JkZXJfd2lkdGgiIDogMSwKICAgICAgICAgICJ0aXRsZSIgOiAiUGxheSIsCiAgICAgICAgICAiYWN0aW9uIiA6ICJQbGF5IiwKICAgICAgICAgICJjbGFzcyIgOiAiQnV0dG9uIiwKICAgICAgICAgICJpbWFnZV9uYW1lIiA6ICJpb2I6cGxheV8yNTYiLAogICAgICAgICAgImZsZXgiIDogIkxSVEIiCiAgICAgICAgfSwKICAgICAgICAic2VsZWN0ZWQiIDogZmFsc2UKICAgICAgfSwKICAgICAgewogICAgICAgICJub2RlcyIgOiBbCgogICAgICAgIF0sCiAgICAgICAgImZyYW1lIiA6ICJ7ezg4LCAyOX0sIHsyMTEsIDM5fX0iLAogICAgICAgICJjbGFzcyIgOiAiVGV4dEZpZWxkIiwKICAgICAgICAiYXR0cmlidXRlcyIgOiB7CiAgICAgICAgICAidXVpZCIgOiAiMDJGM0JGREItNEZENi00MzRFLTlCMDUtRjg3NEIyODU0OTY0IiwKICAgICAgICAgICJiYWNrZ3JvdW5kX2NvbG9yIiA6ICJSR0JBKDAuMTQxMzE5LDAuMTQxMzE5LDAuMTQxMzE5LDEuMDAwMDAwKSIsCiAgICAgICAgICAiZnJhbWUiIDogInt7ODQsIDMwMn0sIHsyMDAsIDMyfX0iLAogICAgICAgICAgInRpbnRfY29sb3IiIDogIlJHQkEoMC4xNDAxMTgsMC4xNDAxMTgsMC4xNDAxMTgsMS4wMDAwMDApIiwKICAgICAgICAgICJhbGlnbm1lbnQiIDogImxlZnQiLAogICAgICAgICAgImF1dG9jb3JyZWN0aW9uX3R5cGUiIDogImRlZmF1bHQiLAogICAgICAgICAgImFjdGlvbiIgOiAiIiwKICAgICAgICAgICJ0ZXh0X2NvbG9yIiA6ICJSR0JBKDEuMDAwMDAwLDAuMDMxMzczLDAuMDMxMzczLDEuMDAwMDAwKSIsCiAgICAgICAgICAicGxhY2Vob2xkZXIiIDogIuODleOCqeODq+ODgOOBruODkeOCueOCkuWFpeWKm+OBl+OBpuOBj+OBoOOBleOBhCIsCiAgICAgICAgICAidGV4dCIgOiAiLiIsCiAgICAgICAgICAiZm9udF9uYW1lIiA6ICI8U3lzdGVtPiIsCiAgICAgICAgICAic3BlbGxjaGVja2luZ190eXBlIiA6ICJkZWZhdWx0IiwKICAgICAgICAgICJjbGFzcyIgOiAiVGV4dEZpZWxkIiwKICAgICAgICAgICJuYW1lIiA6ICJMaWJyYXJ5X1BhdGgiLAogICAgICAgICAgImZvbnRfc2l6ZSIgOiAxNwogICAgICAgIH0sCiAgICAgICAgInNlbGVjdGVkIiA6IGZhbHNlCiAgICAgIH0sCiAgICAgIHsKICAgICAgICAibm9kZXMiIDogWwoKICAgICAgICBdLAogICAgICAgICJmcmFtZSIgOiAie3sxNTIsIDcwLjMzMzMzMzMzMzMzMzM0M30sIHsxNDcsIDQwLjMzMzMzMzMzMzMzMzMyOX19IiwKICAgICAgICAiY2xhc3MiIDogIkxhYmVsIiwKICAgICAgICAiYXR0cmlidXRlcyIgOiB7CiAgICAgICAgICAidXVpZCIgOiAiQjk2RDZDNkYtNTZERi00OTE1LTkxREMtMzAyQThFREE5OUFEIiwKICAgICAgICAgICJmbGV4IiA6ICJXSExSVEIiLAogICAgICAgICAgImNvcm5lcl9yYWRpdXMiIDogMSwKICAgICAgICAgICJiYWNrZ3JvdW5kX2NvbG9yIiA6ICJSR0JBKDAuMTM4OTE3LDAuMTM4OTE3LDAuMTM4OTE3LDEuMDAwMDAwKSIsCiAgICAgICAgICAiZnJhbWUiIDogInt7MTA5LCAzMDJ9LCB7MTUwLCAzMn19IiwKICAgICAgICAgICJib3JkZXJfY29sb3IiIDogIlJHQkEoMC4wMzMyMjAsMC4wMzMyMjAsMC4wMzMyMjAsMS4wMDAwMDApIiwKICAgICAgICAgICJib3JkZXJfd2lkdGgiIDogMSwKICAgICAgICAgICJhbGlnbm1lbnQiIDogImNlbnRlciIsCiAgICAgICAgICAidGV4dF9jb2xvciIgOiAiUkdCQSgxLjAwMDAwMCwwLjAzMTI1MCwwLjAzMTI1MCwxLjAwMDAwMCkiLAogICAgICAgICAgInRleHQiIDogIuODleOCqeODq+ODgOWGhToiLAogICAgICAgICAgImZvbnRfbmFtZSIgOiAiPFN5c3RlbT4iLAogICAgICAgICAgImNsYXNzIiA6ICJMYWJlbCIsCiAgICAgICAgICAibmFtZSIgOiAiIiwKICAgICAgICAgICJmb250X3NpemUiIDogMTgKICAgICAgICB9LAogICAgICAgICJzZWxlY3RlZCIgOiBmYWxzZQogICAgICB9LAogICAgICB7CiAgICAgICAgIm5vZGVzIiA6IFsKCiAgICAgICAgXSwKICAgICAgICAiZnJhbWUiIDogInt7MTYsIDcwfSwgezE0NywgNDB9fSIsCiAgICAgICAgImNsYXNzIiA6ICJUZXh0VmlldyIsCiAgICAgICAgImF0dHJpYnV0ZXMiIDogewogICAgICAgICAgInV1aWQiIDogIjFFOTQ4MjA1LUY2RjUtNDU2Ni1BREFGLUUwNzZGMjBCMUQyRSIsCiAgICAgICAgICAiZm9udF9zaXplIiA6IDExLAogICAgICAgICAgImNvcm5lcl9yYWRpdXMiIDogMSwKICAgICAgICAgICJiYWNrZ3JvdW5kX2NvbG9yIiA6ICJSR0JBKDAuMTQwMTE4LDAuMTQwMTE4LDAuMTQwMTE4LDEuMDAwMDAwKSIsCiAgICAgICAgICAiZnJhbWUiIDogInt7ODQsIDIxOH0sIHsyMDAsIDIwMH19IiwKICAgICAgICAgICJ0aW50X2NvbG9yIiA6ICJSR0JBKDEuMDAwMDAwLDEuMDAwMDAwLDEuMDAwMDAwLDEuMDAwMDAwKSIsCiAgICAgICAgICAiZWRpdGFibGUiIDogZmFsc2UsCiAgICAgICAgICAiYm9yZGVyX2NvbG9yIiA6ICJSR0JBKDAuMDM0NDIxLDAuMDM0NDIxLDAuMDM0NDIxLDEuMDAwMDAwKSIsCiAgICAgICAgICAiYm9yZGVyX3dpZHRoIiA6IDEsCiAgICAgICAgICAiYWxpZ25tZW50IiA6ICJsZWZ0IiwKICAgICAgICAgICJhdXRvY29ycmVjdGlvbl90eXBlIiA6ICJkZWZhdWx0IiwKICAgICAgICAgICJ0ZXh0IiA6ICLpn7Pmpb3jg5XjgqHjgqTjg6vkuIDopqc6XG4o5YaN5bqm6Kqt44G/6L6844G+44Gq44GE44Gn5LiL44GV44GEKSIsCiAgICAgICAgICAidGV4dF9jb2xvciIgOiAiUkdCQSgxLjAwMDAwMCwxLjAwMDAwMCwxLjAwMDAwMCwxLjAwMDAwMCkiLAogICAgICAgICAgImFscGhhIiA6IDEsCiAgICAgICAgICAiZm9udF9uYW1lIiA6ICI8U3lzdGVtPiIsCiAgICAgICAgICAic3BlbGxjaGVja2luZ190eXBlIiA6ICJkZWZhdWx0IiwKICAgICAgICAgICJjbGFzcyIgOiAiVGV4dFZpZXciLAogICAgICAgICAgIm5hbWUiIDogIiIsCiAgICAgICAgICAiZmxleCIgOiAiV0hMUlRCIgogICAgICAgIH0sCiAgICAgICAgInNlbGVjdGVkIiA6IGZhbHNlCiAgICAgIH0sCiAgICAgIHsKICAgICAgICAibm9kZXMiIDogWwoKICAgICAgICBdLAogICAgICAgICJmcmFtZSIgOiAie3sxNiwgMjh9LCB7ODMsIDQwfX0iLAogICAgICAgICJjbGFzcyIgOiAiTGFiZWwiLAogICAgICAgICJhdHRyaWJ1dGVzIiA6IHsKICAgICAgICAgICJuYW1lIiA6ICIiLAogICAgICAgICAgInRleHRfY29sb3IiIDogIlJHQkEoMS4wMDAwMDAsMC4wMDAwMDAsMC4wMDAwMDAsMS4wMDAwMDApIiwKICAgICAgICAgICJmcmFtZSIgOiAie3sxMDksIDMwMn0sIHsxNTAsIDMyfX0iLAogICAgICAgICAgInV1aWQiIDogIjJEQ0FDRjBDLTk4MjUtNDZCNS1CMkVCLUYzMDlBMzI2RkM1NSIsCiAgICAgICAgICAiY2xhc3MiIDogIkxhYmVsIiwKICAgICAgICAgICJhbGlnbm1lbnQiIDogImNlbnRlciIsCiAgICAgICAgICAidGV4dCIgOiAi44OR44K5OiIsCiAgICAgICAgICAiZm9udF9zaXplIiA6IDE4LAogICAgICAgICAgImZvbnRfbmFtZSIgOiAiPFN5c3RlbS1Cb2xkPiIKICAgICAgICB9LAogICAgICAgICJzZWxlY3RlZCIgOiBmYWxzZQogICAgICB9LAogICAgICB7CiAgICAgICAgIm5vZGVzIiA6IFsKCiAgICAgICAgXSwKICAgICAgICAiZnJhbWUiIDogInt7NzYsIDQ5OH0sIHs4MCwgMzJ9fSIsCiAgICAgICAgImNsYXNzIiA6ICJMYWJlbCIsCiAgICAgICAgImF0dHJpYnV0ZXMiIDogewogICAgICAgICAgInV1aWQiIDogIjU2Njk5MkIxLUIwQUMtNDVFNC1CMUQ1LUEyNjNENjNGRTI4RCIsCiAgICAgICAgICAiZm9udF9zaXplIiA6IDE4LAogICAgICAgICAgImNvcm5lcl9yYWRpdXMiIDogMSwKICAgICAgICAgICJmcmFtZSIgOiAie3sxMDksIDMxM30sIHsxNTAsIDMyfX0iLAogICAgICAgICAgImJvcmRlcl9jb2xvciIgOiAiUkdCQSgwLjAzMjAxOSwwLjAzMjAxOSwwLjAzMjAxOSwxLjAwMDAwMCkiLAogICAgICAgICAgImJvcmRlcl93aWR0aCIgOiAxLAogICAgICAgICAgImFsaWdubWVudCIgOiAiY2VudGVyIiwKICAgICAgICAgICJ0ZXh0X2NvbG9yIiA6ICJSR0JBKDEuMDAwMDAwLDAuMDAwMDAwLDAuMDAwMDAwLDEuMDAwMDAwKSIsCiAgICAgICAgICAidGV4dCIgOiAi5YGc5q2iIiwKICAgICAgICAgICJmb250X25hbWUiIDogIjxTeXN0ZW0+IiwKICAgICAgICAgICJjbGFzcyIgOiAiTGFiZWwiLAogICAgICAgICAgIm5hbWUiIDogIiIsCiAgICAgICAgICAiZmxleCIgOiAiTFJUQiIKICAgICAgICB9LAogICAgICAgICJzZWxlY3RlZCIgOiBmYWxzZQogICAgICB9LAogICAgICB7CiAgICAgICAgIm5vZGVzIiA6IFsKCiAgICAgICAgXSwKICAgICAgICAiZnJhbWUiIDogInt7MjA2LCA0OTh9LCB7ODAsIDMyfX0iLAogICAgICAgICJjbGFzcyIgOiAiTGFiZWwiLAogICAgICAgICJhdHRyaWJ1dGVzIiA6IHsKICAgICAgICAgICJ1dWlkIiA6ICI1NjY5OTJCMS1CMEFDLTQ1RTQtQjFENS1BMjYzRDYzRkUyOEQiLAogICAgICAgICAgImZvbnRfc2l6ZSIgOiAxOCwKICAgICAgICAgICJjb3JuZXJfcmFkaXVzIiA6IDEsCiAgICAgICAgICAiZnJhbWUiIDogInt7MTA5LCAzMTN9LCB7MTUwLCAzMn19IiwKICAgICAgICAgICJib3JkZXJfY29sb3IiIDogIlJHQkEoMC4wMzMyMjAsMC4wMzMyMjAsMC4wMzMyMjAsMS4wMDAwMDApIiwKICAgICAgICAgICJib3JkZXJfd2lkdGgiIDogMSwKICAgICAgICAgICJhbGlnbm1lbnQiIDogImNlbnRlciIsCiAgICAgICAgICAidGV4dCIgOiAi5YaN55SfIiwKICAgICAgICAgICJ0ZXh0X2NvbG9yIiA6ICJSR0JBKDEuMDAwMDAwLDAuMDAwMDAwLDAuMDAwMDAwLDEuMDAwMDAwKSIsCiAgICAgICAgICAiZm9udF9uYW1lIiA6ICI8U3lzdGVtPiIsCiAgICAgICAgICAiY2xhc3MiIDogIkxhYmVsIiwKICAgICAgICAgICJuYW1lIiA6ICIiLAogICAgICAgICAgImZsZXgiIDogIkxSVEIiCiAgICAgICAgfSwKICAgICAgICAic2VsZWN0ZWQiIDogZmFsc2UKICAgICAgfSwKICAgICAgewogICAgICAgICJub2RlcyIgOiBbCgogICAgICAgIF0sCiAgICAgICAgImZyYW1lIiA6ICJ7ezE2LCAxMTF9LCB7MzI5LCAyNTN9fSIsCiAgICAgICAgImNsYXNzIiA6ICJUYWJsZVZpZXciLAogICAgICAgICJhdHRyaWJ1dGVzIiA6IHsKICAgICAgICAgICJ1dWlkIiA6ICI4N0MxMEEyNC0zMUE0LTQ5MTYtOEQ4NC05Qzk3QzlFRTc0MUEiLAogICAgICAgICAgImRhdGFfc291cmNlX2FjdGlvbiIgOiAiRmlsZU5hbWUiLAogICAgICAgICAgImJhY2tncm91bmRfY29sb3IiIDogIlJHQkEoMS4wLCAxLjAsIDEuMCwgMS4wKSIsCiAgICAgICAgICAiZnJhbWUiIDogInt7ODQsIDIyOX0sIHsyMDAsIDIwMH19IiwKICAgICAgICAgICJkYXRhX3NvdXJjZV9pdGVtcyIgOiAiIiwKICAgICAgICAgICJkYXRhX3NvdXJjZV9udW1iZXJfb2ZfbGluZXMiIDogMSwKICAgICAgICAgICJkYXRhX3NvdXJjZV9kZWxldGVfZW5hYmxlZCIgOiBmYWxzZSwKICAgICAgICAgICJkYXRhX3NvdXJjZV9mb250X3NpemUiIDogMTgsCiAgICAgICAgICAicm93X2hlaWdodCIgOiA0NCwKICAgICAgICAgICJjbGFzcyIgOiAiVGFibGVWaWV3IiwKICAgICAgICAgICJuYW1lIiA6ICJMaXN0Rm9sZGVycyIsCiAgICAgICAgICAiZmxleCIgOiAiTFJUQiIKICAgICAgICB9LAogICAgICAgICJzZWxlY3RlZCIgOiBmYWxzZQogICAgICB9LAogICAgICB7CiAgICAgICAgIm5vZGVzIiA6IFsKCiAgICAgICAgXSwKICAgICAgICAiZnJhbWUiIDogInt7NiwgMzk4fSwgezE1MCwgOTJ9fSIsCiAgICAgICAgImNsYXNzIiA6ICJUYWJsZVZpZXciLAogICAgICAgICJhdHRyaWJ1dGVzIiA6IHsKICAgICAgICAgICJ1dWlkIiA6ICI5NDcyRTMwNi1BNTU1LTQzQ0ItQUI4Qy01OTVGRUQ2ODAxMUUiLAogICAgICAgICAgImRhdGFfc291cmNlX2FjdGlvbiIgOiAiVGhyZWVEU291bmRNb2RlIiwKICAgICAgICAgICJiYWNrZ3JvdW5kX2NvbG9yIiA6ICJSR0JBKDAuMTQxMTc2LDAuMTQxMTc2LDAuMTQxMTc2LDEuMDAwMDAwKSIsCiAgICAgICAgICAiZnJhbWUiIDogInt7ODQsIDIyOX0sIHsyMDAsIDIwMH19IiwKICAgICAgICAgICJkYXRhX3NvdXJjZV9pdGVtcyIgOiAi56uL5L2T6Z+z6Z+/44KS44Kq44Oz44Gr44GZ44KLXG7nq4vkvZPpn7Ppn7/jgpLjgqrjg5XjgavjgZnjgosiLAogICAgICAgICAgImRhdGFfc291cmNlX251bWJlcl9vZl9saW5lcyIgOiAxLAogICAgICAgICAgInRpbnRfY29sb3IiIDogIlJHQkEoMS4wMDAwMDAsMC4wMzEzNzMsMC4wMzEzNzMsMS4wMDAwMDApIiwKICAgICAgICAgICJkYXRhX3NvdXJjZV9kZWxldGVfZW5hYmxlZCIgOiBmYWxzZSwKICAgICAgICAgICJkYXRhX3NvdXJjZV9mb250X3NpemUiIDogMTIsCiAgICAgICAgICAicm93X2hlaWdodCIgOiA0NCwKICAgICAgICAgICJjbGFzcyIgOiAiVGFibGVWaWV3IiwKICAgICAgICAgICJuYW1lIiA6ICIzRFNvdW5kIiwKICAgICAgICAgICJmbGV4IiA6ICJMUlRCIgogICAgICAgIH0sCiAgICAgICAgInNlbGVjdGVkIiA6IGZhbHNlCiAgICAgIH0sCiAgICAgIHsKICAgICAgICAibm9kZXMiIDogWwoKICAgICAgICBdLAogICAgICAgICJmcmFtZSIgOiAie3sxNiwgMzYzfSwgezMyOSwgMzR9fSIsCiAgICAgICAgImNsYXNzIiA6ICJTbGlkZXIiLAogICAgICAgICJhdHRyaWJ1dGVzIiA6IHsKICAgICAgICAgICJhY3Rpb24iIDogIiIsCiAgICAgICAgICAiZmxleCIgOiAiTFJUQiIsCiAgICAgICAgICAiY29udGludW91cyIgOiB0cnVlLAogICAgICAgICAgImZyYW1lIiA6ICJ7ezg0LCAzMTJ9LCB7MjAwLCAzNH19IiwKICAgICAgICAgICJ0aW50X2NvbG9yIiA6ICJSR0JBKDEuMDAwMDAwLDAuMDMxMzczLDAuMDMxMzczLDEuMDAwMDAwKSIsCiAgICAgICAgICAidXVpZCIgOiAiMDUzOEI0MUQtMkQ0NS00NDg0LTgyQzQtNTVBMTE4RURFQjQ3IiwKICAgICAgICAgICJjbGFzcyIgOiAiU2xpZGVyIiwKICAgICAgICAgICJ2YWx1ZSIgOiAwLAogICAgICAgICAgImJhY2tncm91bmRfY29sb3IiIDogIlJHQkEoMC4xMzcyNTUsMC4xMzcyNTUsMC4xMzcyNTUsMS4wMDAwMDApIiwKICAgICAgICAgICJuYW1lIiA6ICJTZWVrQmFyIgogICAgICAgIH0sCiAgICAgICAgInNlbGVjdGVkIiA6IGZhbHNlCiAgICAgIH0sCiAgICAgIHsKICAgICAgICAibm9kZXMiIDogWwoKICAgICAgICBdLAogICAgICAgICJmcmFtZSIgOiAie3syOTYsIDIwfSwgezY1LCA1NH19IiwKICAgICAgICAiY2xhc3MiIDogIkJ1dHRvbiIsCiAgICAgICAgImF0dHJpYnV0ZXMiIDogewogICAgICAgICAgImFjdGlvbiIgOiAiTGlzdFZpZXciLAogICAgICAgICAgImZsZXgiIDogIkxSVEIiLAogICAgICAgICAgImltYWdlX25hbWUiIDogImlvYjppb3M3X3JlZnJlc2hfZW1wdHlfMjU2IiwKICAgICAgICAgICJmcmFtZSIgOiAie3sxNDQsIDMxM30sIHs4MCwgMzJ9fSIsCiAgICAgICAgICAidGludF9jb2xvciIgOiAiUkdCQSgxLjAwMDAwMCwwLjAzMTM3MywwLjAzMTM3MywxLjAwMDAwMCkiLAogICAgICAgICAgInRpdGxlIiA6ICLjg5Hjgrnjga7oqq3jgb/ovrzjgb8iLAogICAgICAgICAgInV1aWQiIDogIkUzREMzRjEzLTU4RDUtNDUwRi1CNDU5LUUxMTk2MEYwRjU2RiIsCiAgICAgICAgICAiY2xhc3MiIDogIkJ1dHRvbiIsCiAgICAgICAgICAiYmFja2dyb3VuZF9jb2xvciIgOiAiUkdCQSgwLjEzNzI1NSwwLjEzNzI1NSwwLjEzNzI1NSwxLjAwMDAwMCkiLAogICAgICAgICAgImZvbnRfc2l6ZSIgOiA2LAogICAgICAgICAgIm5hbWUiIDogIlJlYWRQYXRoIgogICAgICAgIH0sCiAgICAgICAgInNlbGVjdGVkIiA6IGZhbHNlCiAgICAgIH0KICAgIF0sCiAgICAiZnJhbWUiIDogInt7MCwgMH0sIHszNjcsIDY1OH19IiwKICAgICJjbGFzcyIgOiAiVmlldyIsCiAgICAiYXR0cmlidXRlcyIgOiB7CiAgICAgICJmbGV4IiA6ICIiLAogICAgICAiY3VzdG9tX2NsYXNzIiA6ICJTb3VuZFBsYXllciIsCiAgICAgICJ0aW50X2NvbG9yIiA6ICJSR0JBKDEuMDAwMDAwLDAuMDMxMjUwLDAuMDMxMjUwLDEuMDAwMDAwKSIsCiAgICAgICJlbmFibGVkIiA6IHRydWUsCiAgICAgICJib3JkZXJfY29sb3IiIDogIlJHQkEoMC4wMDAwMDAsMC4wMDAwMDAsMC4wMDAwMDAsMS4wMDAwMDApIiwKICAgICAgImJhY2tncm91bmRfY29sb3IiIDogIlJHQkEoMC4xMDE2ODMsMC4xMDE2ODMsMC4xMDE2ODMsMS4wMDAwMDApIiwKICAgICAgIm5hbWUiIDogIlNvdW5kIFBsYXllciIKICAgIH0sCiAgICAic2VsZWN0ZWQiIDogZmFsc2UKICB9Cl0=').decode()

Mode = ''
SoundMode = ''
NowClosed = ['0']
PlayMusicList = []
_P = None
LDirs = []
LFiles = []

def __init__():
    os.makedirs(os.path.join(os.environ['HOME'], 'Documents', 'AudioFiles'), exist_ok=True)

def ListView(ListsView):
    global Path
    try:
        if ListsView.superview['ListFolders'].data_source.items[0] == '':
            del ListsView.superview['ListFolders'].data_source.items[0]
    except:
        pass
    if not ''.join(ListsView.superview['ListFolders'].data_source.items) == '':
        try:
            Pl = [0]
            for U in Pl:
                for L in range(len(ListsView.superview['ListFolders'].data_source.items)):
                    try:
                        del ListsView.superview['ListFolders'].data_source.items[L]
                    except:
                        Pl.append(U+1)
                if ''.join(ListsView.superview['ListFolders'].data_source.items) == '':
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
        for MFile in sorted(LDirs + LFiles):
            if MFile.split('.')[-1].lower() == 'mp3':
                Musics.append(MFile)
            if MFile.split('.')[-1].lower() == 'm4a':
                Musics.append(MFile)
            if MFile.split('.')[-1].lower() == 'flac':
                Musics.append(MFile)
            if MFile.split('.')[-1].lower() == 'wav':
                Musics.append(MFile)
        ListsView.superview['ListFolders'].data_source.items = sorted(Musics)
    except Exception as W:
        print(W)
        pass

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
    global FileNames
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
    global _P, PlayMusicList
    try:
        if Mode == '':
            Modes = False
        else:
            Modes = Mode
        if SoundMode == '立体音響をオンにする':
            FilePath = os.path.join(Path, FileNames)
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
            FilePath = os.path.join(Path, FileNames)
            PlayMusicList = [sound.Player('{}'.format(FilePath)) for _ in range(1)]
            for Play in PlayMusicList:
                if Modes:
                    Play.play()
                    Play.number_of_loops = -1
                else:
                    Play.play()
        else:
            FilePath = os.path.join(Path, FileNames)
            PlayMusicList = [sound.Player('{}'.format(FilePath)) for _ in range(1)]
            for Play in PlayMusicList:
                if Modes:
                    Play.play()
                    Play.number_of_loops = -1
                else:
                    Play.play()
        Limite = '0'
        """while True:
            Actions(Slider[0])
            for Play in PlayMusicList:
                if not Play.playing:
                    Limite = '1'
            if Limite == '1':
                break"""
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

__init__()
RootDirectoryPath = os.path.join(os.environ['HOME'], 'Documents', 'AudioFiles')
os.chdir(RootDirectoryPath)
s = ui.load_view_str(UIs)
s['Library_Path'].text = RootDirectoryPath.replace(os.environ['HOME'], '~')
s.present('panel')
try:
    while True:
        if NowClosed[0] == '0':
            for Play in PlayMusicList:
                s['SeekBar'].value = int(str(Play.current_time).split('.')[0]) /  int(str(Play.duration).split('.')[0])
        else:
            quit()
except KeyboardInterrupt:
    Stop('0')
    quit()
