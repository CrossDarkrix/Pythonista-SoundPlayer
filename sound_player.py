import ui, sound, os, base64, time, sys
UIs = base64.b64decode('WwogIHsKICAgICJub2RlcyIgOiBbCiAgICAgIHsKICAgICAgICAibm9kZXMiIDogWwoKICAgICAgICBdLAogICAgICAgICJmcmFtZSIgOiAie3sxNTEsIDM5OH0sIHsyMTAsIDkyfX0iLAogICAgICAgICJjbGFzcyIgOiAiVGFibGVWaWV3IiwKICAgICAgICAiYXR0cmlidXRlcyIgOiB7CiAgICAgICAgICAidXVpZCIgOiAiMTBEQjVDMUYtQ0JBOC00NjI3LTkxRDMtOTdGMTQ3OTM2RDhBIiwKICAgICAgICAgICJkYXRhX3NvdXJjZV9hY3Rpb24iIDogIlNlbGVjdG9yIiwKICAgICAgICAgICJiYWNrZ3JvdW5kX2NvbG9yIiA6ICJSR0JBKDAuMTQwMTE4LDAuMTQwMTE4LDAuMTQwMTE4LDEuMDAwMDAwKSIsCiAgICAgICAgICAiZnJhbWUiIDogInt7NTYsIDE4NX0sIHsyMDAsIDIwMH19IiwKICAgICAgICAgICJkYXRhX3NvdXJjZV9pdGVtcyIgOiAiMeODiOODqeODg+OCr+OBruOBv+ODquODlOODvOODiFxu44Oq44OU44O844OI44KS44Kq44OV44Gr44GZ44KLIiwKICAgICAgICAgICJ0aW50X2NvbG9yIiA6ICJSR0JBKDEuMDAwMDAwLDAuMDMxMjUwLDAuMDMxMjUwLDEuMDAwMDAwKSIsCiAgICAgICAgICAiZGF0YV9zb3VyY2VfbnVtYmVyX29mX2xpbmVzIiA6IDEsCiAgICAgICAgICAiZGF0YV9zb3VyY2VfZGVsZXRlX2VuYWJsZWQiIDogZmFsc2UsCiAgICAgICAgICAiZGF0YV9zb3VyY2VfZm9udF9zaXplIiA6IDE4LAogICAgICAgICAgInJvd19oZWlnaHQiIDogNDQsCiAgICAgICAgICAiY2xhc3MiIDogIlRhYmxlVmlldyIsCiAgICAgICAgICAibmFtZSIgOiAiTW9kZV9TZWxlY3QiLAogICAgICAgICAgImZsZXgiIDogIkxSVEIiCiAgICAgICAgfSwKICAgICAgICAic2VsZWN0ZWQiIDogZmFsc2UKICAgICAgfSwKICAgICAgewogICAgICAgICJub2RlcyIgOiBbCgogICAgICAgIF0sCiAgICAgICAgImZyYW1lIiA6ICJ7ezc2LCA1MzV9LCB7ODAsIDgyfX0iLAogICAgICAgICJjbGFzcyIgOiAiQnV0dG9uIiwKICAgICAgICAiYXR0cmlidXRlcyIgOiB7CiAgICAgICAgICAidXVpZCIgOiAiRDYxQzAxODMtRDI2RC00ODRELTk2RTUtNzY3RDdFMjAxMUREIiwKICAgICAgICAgICJpbWFnZV9uYW1lIiA6ICJpb2I6c3RvcF8yNTYiLAogICAgICAgICAgImZvbnRfc2l6ZSIgOiAxNSwKICAgICAgICAgICJjb3JuZXJfcmFkaXVzIiA6IDEsCiAgICAgICAgICAiZnJhbWUiIDogInt7MTE2LCAyNjl9LCB7ODAsIDMyfX0iLAogICAgICAgICAgImJvcmRlcl9jb2xvciIgOiAiUkdCQSgwLjAzMjAxOSwwLjAzMjAxOSwwLjAzMjAxOSwxLjAwMDAwMCkiLAogICAgICAgICAgImJvcmRlcl93aWR0aCIgOiAxLAogICAgICAgICAgInRpdGxlIiA6ICJCdXR0b24iLAogICAgICAgICAgImFjdGlvbiIgOiAiU3RvcCIsCiAgICAgICAgICAiY2xhc3MiIDogIkJ1dHRvbiIsCiAgICAgICAgICAibmFtZSIgOiAiU3RvcCIsCiAgICAgICAgICAiZmxleCIgOiAiTFJUQiIKICAgICAgICB9LAogICAgICAgICJzZWxlY3RlZCIgOiBmYWxzZQogICAgICB9LAogICAgICB7CiAgICAgICAgIm5vZGVzIiA6IFsKCiAgICAgICAgXSwKICAgICAgICAiZnJhbWUiIDogInt7MjA2LCA1MzV9LCB7ODAsIDgyfX0iLAogICAgICAgICJjbGFzcyIgOiAiQnV0dG9uIiwKICAgICAgICAiYXR0cmlidXRlcyIgOiB7CiAgICAgICAgICAidXVpZCIgOiAiRDYxQzAxODMtRDI2RC00ODRELTk2RTUtNzY3RDdFMjAxMUREIiwKICAgICAgICAgICJuYW1lIiA6ICJQbGF5IiwKICAgICAgICAgICJmb250X3NpemUiIDogMTUsCiAgICAgICAgICAiY29ybmVyX3JhZGl1cyIgOiAxLAogICAgICAgICAgImZyYW1lIiA6ICJ7ezExNiwgMjY5fSwgezgwLCAzMn19IiwKICAgICAgICAgICJib3JkZXJfY29sb3IiIDogIlJHQkEoMC4wMzMyMjAsMC4wMzMyMjAsMC4wMzMyMjAsMS4wMDAwMDApIiwKICAgICAgICAgICJib3JkZXJfd2lkdGgiIDogMSwKICAgICAgICAgICJ0aXRsZSIgOiAiUGxheSIsCiAgICAgICAgICAiYWN0aW9uIiA6ICJQbGF5IiwKICAgICAgICAgICJjbGFzcyIgOiAiQnV0dG9uIiwKICAgICAgICAgICJpbWFnZV9uYW1lIiA6ICJpb2I6cGxheV8yNTYiLAogICAgICAgICAgImZsZXgiIDogIkxSVEIiCiAgICAgICAgfSwKICAgICAgICAic2VsZWN0ZWQiIDogZmFsc2UKICAgICAgfSwKICAgICAgewogICAgICAgICJub2RlcyIgOiBbCgogICAgICAgIF0sCiAgICAgICAgImZyYW1lIiA6ICJ7ezg4LCAyOX0sIHsyMTEsIDM5fX0iLAogICAgICAgICJjbGFzcyIgOiAiVGV4dEZpZWxkIiwKICAgICAgICAiYXR0cmlidXRlcyIgOiB7CiAgICAgICAgICAidXVpZCIgOiAiMDJGM0JGREItNEZENi00MzRFLTlCMDUtRjg3NEIyODU0OTY0IiwKICAgICAgICAgICJiYWNrZ3JvdW5kX2NvbG9yIiA6ICJSR0JBKDAuMTQxMzE5LDAuMTQxMzE5LDAuMTQxMzE5LDEuMDAwMDAwKSIsCiAgICAgICAgICAiZnJhbWUiIDogInt7ODQsIDMwMn0sIHsyMDAsIDMyfX0iLAogICAgICAgICAgInRpbnRfY29sb3IiIDogIlJHQkEoMC4xNDAxMTgsMC4xNDAxMTgsMC4xNDAxMTgsMS4wMDAwMDApIiwKICAgICAgICAgICJhbGlnbm1lbnQiIDogImxlZnQiLAogICAgICAgICAgImF1dG9jb3JyZWN0aW9uX3R5cGUiIDogImRlZmF1bHQiLAogICAgICAgICAgImFjdGlvbiIgOiAiIiwKICAgICAgICAgICJ0ZXh0X2NvbG9yIiA6ICJSR0JBKDEuMDAwMDAwLDEuMDAwMDAwLDEuMDAwMDAwLDEuMDAwMDAwKSIsCiAgICAgICAgICAicGxhY2Vob2xkZXIiIDogIuODleOCqeODq+ODgOOBruODkeOCueOCkuWFpeWKm+OBl+OBpuOBj+OBoOOBleOBhCIsCiAgICAgICAgICAidGV4dCIgOiAiLiIsCiAgICAgICAgICAiZm9udF9uYW1lIiA6ICI8U3lzdGVtPiIsCiAgICAgICAgICAic3BlbGxjaGVja2luZ190eXBlIiA6ICJkZWZhdWx0IiwKICAgICAgICAgICJjbGFzcyIgOiAiVGV4dEZpZWxkIiwKICAgICAgICAgICJuYW1lIiA6ICJMaWJyYXJ5X1BhdGgiLAogICAgICAgICAgImZvbnRfc2l6ZSIgOiAxNwogICAgICAgIH0sCiAgICAgICAgInNlbGVjdGVkIiA6IHRydWUKICAgICAgfSwKICAgICAgewogICAgICAgICJub2RlcyIgOiBbCgogICAgICAgIF0sCiAgICAgICAgImZyYW1lIiA6ICJ7ezE1MiwgNzAuMzMzMzMzMzMzMzMzMzQzfSwgezE0NywgNDAuMzMzMzMzMzMzMzMzMzI5fX0iLAogICAgICAgICJjbGFzcyIgOiAiTGFiZWwiLAogICAgICAgICJhdHRyaWJ1dGVzIiA6IHsKICAgICAgICAgICJ1dWlkIiA6ICJCOTZENkM2Ri01NkRGLTQ5MTUtOTFEQy0zMDJBOEVEQTk5QUQiLAogICAgICAgICAgImZsZXgiIDogIldITFJUQiIsCiAgICAgICAgICAiY29ybmVyX3JhZGl1cyIgOiAxLAogICAgICAgICAgImJhY2tncm91bmRfY29sb3IiIDogIlJHQkEoMC4xMzg5MTcsMC4xMzg5MTcsMC4xMzg5MTcsMS4wMDAwMDApIiwKICAgICAgICAgICJmcmFtZSIgOiAie3sxMDksIDMwMn0sIHsxNTAsIDMyfX0iLAogICAgICAgICAgImJvcmRlcl9jb2xvciIgOiAiUkdCQSgwLjAzMzIyMCwwLjAzMzIyMCwwLjAzMzIyMCwxLjAwMDAwMCkiLAogICAgICAgICAgImJvcmRlcl93aWR0aCIgOiAxLAogICAgICAgICAgImFsaWdubWVudCIgOiAiY2VudGVyIiwKICAgICAgICAgICJ0ZXh0X2NvbG9yIiA6ICJSR0JBKDEuMDAwMDAwLDAuMDMxMjUwLDAuMDMxMjUwLDEuMDAwMDAwKSIsCiAgICAgICAgICAidGV4dCIgOiAi44OV44Kp44Or44OA5YaFOiIsCiAgICAgICAgICAiZm9udF9uYW1lIiA6ICI8U3lzdGVtPiIsCiAgICAgICAgICAiY2xhc3MiIDogIkxhYmVsIiwKICAgICAgICAgICJuYW1lIiA6ICIiLAogICAgICAgICAgImZvbnRfc2l6ZSIgOiAxOAogICAgICAgIH0sCiAgICAgICAgInNlbGVjdGVkIiA6IGZhbHNlCiAgICAgIH0sCiAgICAgIHsKICAgICAgICAibm9kZXMiIDogWwoKICAgICAgICBdLAogICAgICAgICJmcmFtZSIgOiAie3sxNiwgNzB9LCB7MTQ3LCA0MH19IiwKICAgICAgICAiY2xhc3MiIDogIlRleHRWaWV3IiwKICAgICAgICAiYXR0cmlidXRlcyIgOiB7CiAgICAgICAgICAidXVpZCIgOiAiMUU5NDgyMDUtRjZGNS00NTY2LUFEQUYtRTA3NkYyMEIxRDJFIiwKICAgICAgICAgICJmb250X3NpemUiIDogMTEsCiAgICAgICAgICAiY29ybmVyX3JhZGl1cyIgOiAxLAogICAgICAgICAgImJhY2tncm91bmRfY29sb3IiIDogIlJHQkEoMC4xNDAxMTgsMC4xNDAxMTgsMC4xNDAxMTgsMS4wMDAwMDApIiwKICAgICAgICAgICJmcmFtZSIgOiAie3s4NCwgMjE4fSwgezIwMCwgMjAwfX0iLAogICAgICAgICAgInRpbnRfY29sb3IiIDogIlJHQkEoMS4wMDAwMDAsMS4wMDAwMDAsMS4wMDAwMDAsMS4wMDAwMDApIiwKICAgICAgICAgICJlZGl0YWJsZSIgOiBmYWxzZSwKICAgICAgICAgICJib3JkZXJfY29sb3IiIDogIlJHQkEoMC4wMzQ0MjEsMC4wMzQ0MjEsMC4wMzQ0MjEsMS4wMDAwMDApIiwKICAgICAgICAgICJib3JkZXJfd2lkdGgiIDogMSwKICAgICAgICAgICJhbGlnbm1lbnQiIDogImxlZnQiLAogICAgICAgICAgImF1dG9jb3JyZWN0aW9uX3R5cGUiIDogImRlZmF1bHQiLAogICAgICAgICAgInRleHQiIDogIumfs+alveODleOCoeOCpOODq+S4gOimpzpcbijlho3luqboqq3jgb/ovrzjgb7jgarjgYTjgafkuIvjgZXjgYQpIiwKICAgICAgICAgICJ0ZXh0X2NvbG9yIiA6ICJSR0JBKDEuMDAwMDAwLDEuMDAwMDAwLDEuMDAwMDAwLDEuMDAwMDAwKSIsCiAgICAgICAgICAiYWxwaGEiIDogMSwKICAgICAgICAgICJmb250X25hbWUiIDogIjxTeXN0ZW0+IiwKICAgICAgICAgICJzcGVsbGNoZWNraW5nX3R5cGUiIDogImRlZmF1bHQiLAogICAgICAgICAgImNsYXNzIiA6ICJUZXh0VmlldyIsCiAgICAgICAgICAibmFtZSIgOiAiIiwKICAgICAgICAgICJmbGV4IiA6ICJXSExSVEIiCiAgICAgICAgfSwKICAgICAgICAic2VsZWN0ZWQiIDogZmFsc2UKICAgICAgfSwKICAgICAgewogICAgICAgICJub2RlcyIgOiBbCgogICAgICAgIF0sCiAgICAgICAgImZyYW1lIiA6ICJ7ezE2LCAyOH0sIHs4MywgNDB9fSIsCiAgICAgICAgImNsYXNzIiA6ICJMYWJlbCIsCiAgICAgICAgImF0dHJpYnV0ZXMiIDogewogICAgICAgICAgIm5hbWUiIDogIiIsCiAgICAgICAgICAidGV4dF9jb2xvciIgOiAiUkdCQSgxLjAwMDAwMCwwLjAwMDAwMCwwLjAwMDAwMCwxLjAwMDAwMCkiLAogICAgICAgICAgImZyYW1lIiA6ICJ7ezEwOSwgMzAyfSwgezE1MCwgMzJ9fSIsCiAgICAgICAgICAidXVpZCIgOiAiMkRDQUNGMEMtOTgyNS00NkI1LUIyRUItRjMwOUEzMjZGQzU1IiwKICAgICAgICAgICJjbGFzcyIgOiAiTGFiZWwiLAogICAgICAgICAgImFsaWdubWVudCIgOiAiY2VudGVyIiwKICAgICAgICAgICJ0ZXh0IiA6ICLjg5Hjgrk6IiwKICAgICAgICAgICJmb250X3NpemUiIDogMTgsCiAgICAgICAgICAiZm9udF9uYW1lIiA6ICI8U3lzdGVtLUJvbGQ+IgogICAgICAgIH0sCiAgICAgICAgInNlbGVjdGVkIiA6IGZhbHNlCiAgICAgIH0sCiAgICAgIHsKICAgICAgICAibm9kZXMiIDogWwoKICAgICAgICBdLAogICAgICAgICJmcmFtZSIgOiAie3s3NiwgNDk4fSwgezgwLCAzMn19IiwKICAgICAgICAiY2xhc3MiIDogIkxhYmVsIiwKICAgICAgICAiYXR0cmlidXRlcyIgOiB7CiAgICAgICAgICAidXVpZCIgOiAiNTY2OTkyQjEtQjBBQy00NUU0LUIxRDUtQTI2M0Q2M0ZFMjhEIiwKICAgICAgICAgICJmb250X3NpemUiIDogMTgsCiAgICAgICAgICAiY29ybmVyX3JhZGl1cyIgOiAxLAogICAgICAgICAgImZyYW1lIiA6ICJ7ezEwOSwgMzEzfSwgezE1MCwgMzJ9fSIsCiAgICAgICAgICAiYm9yZGVyX2NvbG9yIiA6ICJSR0JBKDAuMDMyMDE5LDAuMDMyMDE5LDAuMDMyMDE5LDEuMDAwMDAwKSIsCiAgICAgICAgICAiYm9yZGVyX3dpZHRoIiA6IDEsCiAgICAgICAgICAiYWxpZ25tZW50IiA6ICJjZW50ZXIiLAogICAgICAgICAgInRleHRfY29sb3IiIDogIlJHQkEoMS4wMDAwMDAsMC4wMDAwMDAsMC4wMDAwMDAsMS4wMDAwMDApIiwKICAgICAgICAgICJ0ZXh0IiA6ICLlgZzmraIiLAogICAgICAgICAgImZvbnRfbmFtZSIgOiAiPFN5c3RlbT4iLAogICAgICAgICAgImNsYXNzIiA6ICJMYWJlbCIsCiAgICAgICAgICAibmFtZSIgOiAiIiwKICAgICAgICAgICJmbGV4IiA6ICJMUlRCIgogICAgICAgIH0sCiAgICAgICAgInNlbGVjdGVkIiA6IGZhbHNlCiAgICAgIH0sCiAgICAgIHsKICAgICAgICAibm9kZXMiIDogWwoKICAgICAgICBdLAogICAgICAgICJmcmFtZSIgOiAie3syMDYsIDQ5OH0sIHs4MCwgMzJ9fSIsCiAgICAgICAgImNsYXNzIiA6ICJMYWJlbCIsCiAgICAgICAgImF0dHJpYnV0ZXMiIDogewogICAgICAgICAgInV1aWQiIDogIjU2Njk5MkIxLUIwQUMtNDVFNC1CMUQ1LUEyNjNENjNGRTI4RCIsCiAgICAgICAgICAiZm9udF9zaXplIiA6IDE4LAogICAgICAgICAgImNvcm5lcl9yYWRpdXMiIDogMSwKICAgICAgICAgICJmcmFtZSIgOiAie3sxMDksIDMxM30sIHsxNTAsIDMyfX0iLAogICAgICAgICAgImJvcmRlcl9jb2xvciIgOiAiUkdCQSgwLjAzMzIyMCwwLjAzMzIyMCwwLjAzMzIyMCwxLjAwMDAwMCkiLAogICAgICAgICAgImJvcmRlcl93aWR0aCIgOiAxLAogICAgICAgICAgImFsaWdubWVudCIgOiAiY2VudGVyIiwKICAgICAgICAgICJ0ZXh0IiA6ICLlho3nlJ8iLAogICAgICAgICAgInRleHRfY29sb3IiIDogIlJHQkEoMS4wMDAwMDAsMC4wMDAwMDAsMC4wMDAwMDAsMS4wMDAwMDApIiwKICAgICAgICAgICJmb250X25hbWUiIDogIjxTeXN0ZW0+IiwKICAgICAgICAgICJjbGFzcyIgOiAiTGFiZWwiLAogICAgICAgICAgIm5hbWUiIDogIiIsCiAgICAgICAgICAiZmxleCIgOiAiTFJUQiIKICAgICAgICB9LAogICAgICAgICJzZWxlY3RlZCIgOiBmYWxzZQogICAgICB9LAogICAgICB7CiAgICAgICAgIm5vZGVzIiA6IFsKCiAgICAgICAgXSwKICAgICAgICAiZnJhbWUiIDogInt7MTYsIDExMX0sIHszMjksIDI1M319IiwKICAgICAgICAiY2xhc3MiIDogIlRhYmxlVmlldyIsCiAgICAgICAgImF0dHJpYnV0ZXMiIDogewogICAgICAgICAgInV1aWQiIDogIjg3QzEwQTI0LTMxQTQtNDkxNi04RDg0LTlDOTdDOUVFNzQxQSIsCiAgICAgICAgICAiZGF0YV9zb3VyY2VfYWN0aW9uIiA6ICJGaWxlTmFtZSIsCiAgICAgICAgICAiYmFja2dyb3VuZF9jb2xvciIgOiAiUkdCQSgxLjAsIDEuMCwgMS4wLCAxLjApIiwKICAgICAgICAgICJmcmFtZSIgOiAie3s4NCwgMjI5fSwgezIwMCwgMjAwfX0iLAogICAgICAgICAgImRhdGFfc291cmNlX2l0ZW1zIiA6ICIiLAogICAgICAgICAgImRhdGFfc291cmNlX251bWJlcl9vZl9saW5lcyIgOiAxLAogICAgICAgICAgImRhdGFfc291cmNlX2RlbGV0ZV9lbmFibGVkIiA6IGZhbHNlLAogICAgICAgICAgImRhdGFfc291cmNlX2ZvbnRfc2l6ZSIgOiAxOCwKICAgICAgICAgICJyb3dfaGVpZ2h0IiA6IDQ0LAogICAgICAgICAgImNsYXNzIiA6ICJUYWJsZVZpZXciLAogICAgICAgICAgIm5hbWUiIDogIkxpc3RGb2xkZXJzIiwKICAgICAgICAgICJmbGV4IiA6ICJMUlRCIgogICAgICAgIH0sCiAgICAgICAgInNlbGVjdGVkIiA6IGZhbHNlCiAgICAgIH0sCiAgICAgIHsKICAgICAgICAibm9kZXMiIDogWwoKICAgICAgICBdLAogICAgICAgICJmcmFtZSIgOiAie3s2LCAzOTh9LCB7MTUwLCA5Mn19IiwKICAgICAgICAiY2xhc3MiIDogIlRhYmxlVmlldyIsCiAgICAgICAgImF0dHJpYnV0ZXMiIDogewogICAgICAgICAgInV1aWQiIDogIjk0NzJFMzA2LUE1NTUtNDNDQi1BQjhDLTU5NUZFRDY4MDExRSIsCiAgICAgICAgICAiZGF0YV9zb3VyY2VfYWN0aW9uIiA6ICJUaHJlZURTb3VuZE1vZGUiLAogICAgICAgICAgImJhY2tncm91bmRfY29sb3IiIDogIlJHQkEoMC4xNDExNzYsMC4xNDExNzYsMC4xNDExNzYsMS4wMDAwMDApIiwKICAgICAgICAgICJmcmFtZSIgOiAie3s4NCwgMjI5fSwgezIwMCwgMjAwfX0iLAogICAgICAgICAgImRhdGFfc291cmNlX2l0ZW1zIiA6ICLnq4vkvZPpn7Ppn7/jgpLjgqrjg7PjgavjgZnjgotcbueri+S9k+mfs+mfv+OCkuOCquODleOBq+OBmeOCiyIsCiAgICAgICAgICAiZGF0YV9zb3VyY2VfbnVtYmVyX29mX2xpbmVzIiA6IDEsCiAgICAgICAgICAidGludF9jb2xvciIgOiAiUkdCQSgxLjAwMDAwMCwwLjAzMTM3MywwLjAzMTM3MywxLjAwMDAwMCkiLAogICAgICAgICAgImRhdGFfc291cmNlX2RlbGV0ZV9lbmFibGVkIiA6IGZhbHNlLAogICAgICAgICAgImRhdGFfc291cmNlX2ZvbnRfc2l6ZSIgOiAxMiwKICAgICAgICAgICJyb3dfaGVpZ2h0IiA6IDQ0LAogICAgICAgICAgImNsYXNzIiA6ICJUYWJsZVZpZXciLAogICAgICAgICAgIm5hbWUiIDogIjNEU291bmQiLAogICAgICAgICAgImZsZXgiIDogIkxSVEIiCiAgICAgICAgfSwKICAgICAgICAic2VsZWN0ZWQiIDogZmFsc2UKICAgICAgfSwKICAgICAgewogICAgICAgICJub2RlcyIgOiBbCgogICAgICAgIF0sCiAgICAgICAgImZyYW1lIiA6ICJ7ezE2LCAzNjN9LCB7MzI5LCAzNH19IiwKICAgICAgICAiY2xhc3MiIDogIlNsaWRlciIsCiAgICAgICAgImF0dHJpYnV0ZXMiIDogewogICAgICAgICAgImFjdGlvbiIgOiAiIiwKICAgICAgICAgICJmbGV4IiA6ICJMUlRCIiwKICAgICAgICAgICJjb250aW51b3VzIiA6IHRydWUsCiAgICAgICAgICAiZnJhbWUiIDogInt7ODQsIDMxMn0sIHsyMDAsIDM0fX0iLAogICAgICAgICAgInRpbnRfY29sb3IiIDogIlJHQkEoMS4wMDAwMDAsMC4wMzEzNzMsMC4wMzEzNzMsMS4wMDAwMDApIiwKICAgICAgICAgICJ1dWlkIiA6ICIwNTM4QjQxRC0yRDQ1LTQ0ODQtODJDNC01NUExMThFREVCNDciLAogICAgICAgICAgImNsYXNzIiA6ICJTbGlkZXIiLAogICAgICAgICAgInZhbHVlIiA6IDAsCiAgICAgICAgICAiYmFja2dyb3VuZF9jb2xvciIgOiAiUkdCQSgwLjEzNzI1NSwwLjEzNzI1NSwwLjEzNzI1NSwxLjAwMDAwMCkiLAogICAgICAgICAgIm5hbWUiIDogIlNlZWtCYXIiCiAgICAgICAgfSwKICAgICAgICAic2VsZWN0ZWQiIDogZmFsc2UKICAgICAgfSwKICAgICAgewogICAgICAgICJub2RlcyIgOiBbCgogICAgICAgIF0sCiAgICAgICAgImZyYW1lIiA6ICJ7ezI5NiwgMjB9LCB7NjUsIDU0fX0iLAogICAgICAgICJjbGFzcyIgOiAiQnV0dG9uIiwKICAgICAgICAiYXR0cmlidXRlcyIgOiB7CiAgICAgICAgICAiYWN0aW9uIiA6ICJMaXN0VmlldyIsCiAgICAgICAgICAiZmxleCIgOiAiTFJUQiIsCiAgICAgICAgICAiaW1hZ2VfbmFtZSIgOiAiaW9iOmlvczdfcmVmcmVzaF9lbXB0eV8yNTYiLAogICAgICAgICAgImZyYW1lIiA6ICJ7ezE0NCwgMzEzfSwgezgwLCAzMn19IiwKICAgICAgICAgICJ0aW50X2NvbG9yIiA6ICJSR0JBKDEuMDAwMDAwLDAuMDMxMzczLDAuMDMxMzczLDEuMDAwMDAwKSIsCiAgICAgICAgICAidGl0bGUiIDogIuODkeOCueOBruiqreOBv+i+vOOBvyIsCiAgICAgICAgICAidXVpZCIgOiAiRTNEQzNGMTMtNThENS00NTBGLUI0NTktRTExOTYwRjBGNTZGIiwKICAgICAgICAgICJjbGFzcyIgOiAiQnV0dG9uIiwKICAgICAgICAgICJiYWNrZ3JvdW5kX2NvbG9yIiA6ICJSR0JBKDAuMTM3MjU1LDAuMTM3MjU1LDAuMTM3MjU1LDEuMDAwMDAwKSIsCiAgICAgICAgICAibmFtZSIgOiAiUmVhZFBhdGgiLAogICAgICAgICAgImZvbnRfc2l6ZSIgOiA2CiAgICAgICAgfSwKICAgICAgICAic2VsZWN0ZWQiIDogZmFsc2UKICAgICAgfQogICAgXSwKICAgICJmcmFtZSIgOiAie3swLCAwfSwgezM2NywgNjU4fX0iLAogICAgImNsYXNzIiA6ICJWaWV3IiwKICAgICJhdHRyaWJ1dGVzIiA6IHsKICAgICAgImZsZXgiIDogIiIsCiAgICAgICJjdXN0b21fY2xhc3MiIDogIlNvdW5kUGxheWVyIiwKICAgICAgInRpbnRfY29sb3IiIDogIlJHQkEoMS4wMDAwMDAsMC4wMzEyNTAsMC4wMzEyNTAsMS4wMDAwMDApIiwKICAgICAgImVuYWJsZWQiIDogdHJ1ZSwKICAgICAgImJvcmRlcl9jb2xvciIgOiAiUkdCQSgwLjAwMDAwMCwwLjAwMDAwMCwwLjAwMDAwMCwxLjAwMDAwMCkiLAogICAgICAiYmFja2dyb3VuZF9jb2xvciIgOiAiUkdCQSgwLjEwMTY4MywwLjEwMTY4MywwLjEwMTY4MywxLjAwMDAwMCkiLAogICAgICAibmFtZSIgOiAiU291bmQgUGxheWVyIgogICAgfSwKICAgICJzZWxlY3RlZCIgOiBmYWxzZQogIH0KXQ==').decode()

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
