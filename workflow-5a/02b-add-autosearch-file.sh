#!/usr/bin/env bash
set -e

source config.sh

curl \
  "$AUTOSEARCH_HOST/${USERNAME}:${COLLECTION}/docs" \
  --form "data=@${FILENAME_FOLIA}" \
  --header "X-BlackLabAccessToken: $BLACK_LAB_ACCESS_TOKEN" \
  --header "X-BlackLabUserId: $USERNAME" \

echo -e "\n\nFile added. Open https://portal.clarin.inl.nl/autocorp-vre/corpora to explore your corpus"
