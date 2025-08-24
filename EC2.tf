resource "aws_instance" "my_ec2" {
  ami           = "ami-0c55b159cbfafe1f0" # Amazon Linux 2 AMI (check region-specific AMI ID)
  instance_type = "t2.micro"              # Free tier eligible

  tags = {
    Name = "MyTerraformEC2"
  }
}
