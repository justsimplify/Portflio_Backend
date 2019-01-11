docker stop basic && \
docker rm basic && \
docker rmi himanshu-basic-details && \
cd basics/ && docker build -t himanshu-basic-details:latest . && \
docker run -d -p 5000:5000 --name=basic himanshu-basic-details && \
cd ..

docker stop education && \
docker rm education && \
docker rmi himanshu-education-details && \
cd education/ && docker build -t himanshu-education-details:latest . && \
docker run -d -p 4000:5000 --name=education himanshu-education-details && \
cd ..

docker stop skills && \
docker rm skills && \
docker rmi himanshu-skills-details && \
cd skills/ && docker build -t himanshu-skills-details:latest . && \
docker run -d -p 1000:5000 --name=skills himanshu-skills-details && \
cd ..

docker stop experience && \
docker rm experience && \
docker rmi himanshu-experience-details && \
cd experience/ && docker build -t himanshu-experience-details:latest . && \
docker run -d -p 3000:5000 --name=experience himanshu-experience-details && \
cd ..

docker stop projects
docker rm projects
docker rmi himanshu-projects-details
cd projects/ && docker build -t himanshu-projects-details:latest .
docker run -d -p 2000:5000 --name=projects himanshu-projects-details
cd ..