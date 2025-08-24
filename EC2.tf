resource "aws_instance" "my_ec2" {
  ami           = "ami-0c55b159cbfafe1f0" # Amazon Linux 2 AMI (check region-specific AMI ID)
  instance_type = "t2.micro"              # Free tier eligible

  tags = {
    Name = "MyTerraformEC2"
  }
}
resource "aws_db_instance" "mydb" {
  allocated_storage    = 20
  engine               = "mysql"
  engine_version       = "8.0"
  instance_class       = "db.t3.micro"
  name                 = "mydatabase"
  username             = "admin"
  password             = "Password123!"  # change to a secure password
  parameter_group_name = "default.mysql8.0"
  skip_final_snapshot  = true

  publicly_accessible = true  # for testing, set false for production

  tags = {
    Name = "TerraformRDS"
  }
}
