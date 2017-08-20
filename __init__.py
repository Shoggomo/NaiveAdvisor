import rest_api
from core import supervisor


def supervisor_ready(supervisor):
    rest_api.run(supervisor)


def main():
    supervisor.SuperVisor(supervisor_ready)

if __name__ == "__main__":
    main()
