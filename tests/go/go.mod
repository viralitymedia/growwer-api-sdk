module github.com/viralitymedia/growwer-api-sdk/tests/go

go 1.23

require github.com/viralitymedia/growwer-api-sdk/go v0.0.0

require gopkg.in/validator.v2 v2.0.1 // indirect

// The fixture tests exercise the client in this checkout, not a published version.
replace github.com/viralitymedia/growwer-api-sdk/go => ../../go
