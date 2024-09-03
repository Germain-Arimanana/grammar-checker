import streamlit as st
import language_tool_python

# Set up the LanguageTool for French
tool = language_tool_python.LanguageTool('fr')

st.title("Correcteur Grammatical Français")

st.write("Entrez votre texte en français pour vérifier la grammaire et l'orthographe.")

# Text area for input
text = st.text_area("Texte à vérifier", height=200)

# Button to check the text
if st.button("Vérifier la grammaire"):
    # Check for grammar and spelling mistakes
    matches = tool.check(text)
    
    if len(matches) == 0:
        st.success("Aucune erreur trouvée!")
    else:
        st.write("Erreurs détectées:")
        for match in matches:
            st.write(f"Erreur: {match.message}")
            st.write(f"Suggestion: {', '.join(match.replacements)}")
            st.write(f"Contexte: {match.context}")
            st.write("---")

st.write("Merci d'utiliser notre correcteur grammatical!")

