#!/bin/bash

DIRECTORY="katas"
mkdir -p "$DIRECTORY"

# Función para mostrar ayuda
show_help() {
  echo "🥋 SENSEI - Tu guía en el Coding Dojo"
  echo "-------------------------------------"
  echo "Uso:"
  echo "  ./sensei.sh -m \"ID. Nombre\"  -> [M]editar: Crear nueva Kata"
  echo "  ./sensei.sh -e <ID>            -> [E]ntrenar: Ejecutar tests de la Kata"
  echo "  ./sensei.sh -l                 -> [L]istar: Ver tus Katas completadas"
  echo ""
  echo "Ejemplos:"
  echo "  ./sensei.sh -m \"14. Longest Common Prefix\""
  echo "  ./sensei.sh -e 14"
  exit 1
}

# Si no hay argumentos, mostrar ayuda
if [ $# -eq 0 ]; then
  show_help
fi

OPTION=$1
VALUE=$2

case $OPTION in
-m | --meditar)
  # --- MODO CREACIÓN ---
  INPUT=$VALUE
  NUMBER=$(echo "$INPUT" | grep -oE '^[0-9]+')
  PROBLEM_NAME=$(echo "$INPUT" | sed -E 's/^[0-9]+\.? *//')
  FUNCTION_NAME=$(echo "$PROBLEM_NAME" | tr '[:upper:]' '[:lower:]' | sed 's/[^a-z0-9 ]//g' | sed 's/  */_/g' | sed 's/ /_/g')

  if [ -z "$NUMBER" ] || [ -z "$PROBLEM_NAME" ]; then
    echo "❌ Error: Formato inválido. Usa \"ID. Nombre\""
    exit 1
  fi

  FILE_PATH="${DIRECTORY}/${NUMBER}.py"

  if [ -f "$FILE_PATH" ]; then
    echo "⚠️  Esa Kata ya existe en tu Dojo. ¡Sigue entrenando!"
  else
    cat <<EOF >"$FILE_PATH"
import pytest
from utils.log import Log
from typing import List, Dict, Optional

#
# $PROBLEM_NAME
#
class Solution:
    def solve(self, *args, **kwargs):
        # Implementa tu solución aquí
        pass

# Unit tests

@pytest.mark.parametrize(
    "params, expected",
    [
        # (input, output),
    ],
)
def test_${FUNCTION_NAME}(params, expected):
    sol = Solution()
    # assert sol.solve(params) == expected
EOF
    echo "🥋 Kata $NUMBER preparada para meditación en: $FILE_PATH"
  fi
  ;;

-e | --entrenar)
  # --- MODO EJECUCIÓN ---
  FILE_PATH="${DIRECTORY}/${VALUE}.py"
  if [ -f "$FILE_PATH" ]; then
    echo "⚔️  Entrenando Kata $VALUE..."
    pytest "$FILE_PATH" -v
  else
    echo "❌ Error: La Kata $VALUE no existe."
  fi
  ;;

-l | --listar)
  # --- MODO LISTAR ---
  echo "📜 Registro de Katas en el Dojo:"
  echo "--------------------------------"
  # Lista archivos .py, extrae el número y el nombre que está en el comentario
  ls $DIRECTORY/*.py 2>/dev/null | sort -V | while read -r file; do
    ID=$(basename "$file" .py)
    # Extrae la primera línea después de 'class Solution' o el comentario inicial
    NAME=$(grep -m 1 "#" "$file" | sed 's/#//' | xargs)
    printf "  %-4s | %s\n" "$ID" "$NAME"
  done
  ;;

*)
  show_help
  ;;
esac
