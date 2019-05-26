resource "aws_iam_role" "lambda_dynamo" {
  name = "lambda-dynamodb-cloudgoat"

  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Effect": "Allow",
      "Sid": ""
    }
  ]
}
EOF
}

resource "aws_iam_role_policy" "lambda_dynamo_iam_policy" {
  name = "policy_for_lambda_dynamo_role"
  role = "${aws_iam_role.lambda_dynamo.id}"

  policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": [
        "iam:DeleteRolePolicy",
        "logs:*",
        "iam:ListRoles",
        "dynamodb:*",
        "iam:AttachRolePolicy"
      ],
      "Effect": "Allow",
      "Resource": "*"
    }
  ]
}
EOF
}
