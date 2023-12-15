# Use an official Python runtime as a parent image
FROM python:3.10

# Set the working directory in the container to /app
WORKDIR /app

# Add the current directory contents into the container at /app
ADD App /app

# 数据库稳定性不太好，所以先注释掉
#ENV MYSQL_USER=youruser
#ENV MYSQL_PASSWORD=yourpassword

#RUN mysql -u $MYSQL_USER -p$MYSQL_PASSWORD online_interview_system < /docker-entrypoint-initdb.d/online_interview_system.sql
#
## Install MySQL client
#RUN apt-get update && apt-get install -y mysql-client
#
## Copy your database dump into the Docker image
#COPY your-database-dump.sql /docker-entrypoint-initdb.d/

# Import the database
# RUN mysql -u youruser -p yourpassword yourdatabase < /docker-entrypoint-initdb.d/your-database-dump.sql

# 下载库有时会失败
# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

# https 使用端口
# Make port 443 available to the world outside this container
EXPOSE 443

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "app.py"]