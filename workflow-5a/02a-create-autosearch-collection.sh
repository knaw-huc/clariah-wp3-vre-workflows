#!/usr/bin/env bash
set -x
source config.sh

curl "$AUTOSEARCH_HOST/${USERNAME_ESCAPED}%3A${COLLECTION}?outputformat=json" \
  --request DELETE \
  --header "X-BlackLabAccessToken: $BLACK_LAB_ACCESS_TOKEN" \
  --header "X-BlackLabUserId: $USERNAME"

curl "$AUTOSEARCH_HOST/?outputformat=json" \
  --request POST \
  --data-urlencode "name=${USERNAME}:${COLLECTION}" \
  --data-urlencode "display=${COLLECTION}" \
  --data-urlencode "format=folia" \
  --header "X-BlackLabAccessToken: $BLACK_LAB_ACCESS_TOKEN" \
  --header "X-BlackLabUserId: $USERNAME"
