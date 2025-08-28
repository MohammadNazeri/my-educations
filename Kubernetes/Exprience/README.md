# Share exprience 
## check logs inside of pod
// run the test pod
kubectl run test-health --rm -i --tty --image=curlimages/curl -- sh
// get the token
curl -k -d "grant_type=client_credentials" -H "Authorization: Basic N2syOWc0NjJja212ZWVrdTEzZjAxYmM1dnM6MXU5cW9lcXFyMDc2N28xZHZuZ2ltNHJhY2Ywam1tYXFqa2kzNXM0bW1lYTY2Y2k4ZjZ2MA==" https://cx-test.auth.eu-west-1.amazoncognito.com/oauth2/token
// set var
export JWT_TOKEN=eyJraWQ...
// call url
curl -k -X 'POST' \
  'http://cx-santi-web-chat-service.cx-santi.svc.cluster.local:3000/api/message' \
  -H "Authorization: Bearer $JWT_TOKEN" \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "message": "what is eco?"
}'
 
