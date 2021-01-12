from config import Config
from utils import *

if __name__ == '__main__':
    cfg = Config()
    cfg.from_pyfile("config_my.py")

    interval = np.arange(10, 101, step=10)

    plt.figure(figsize=(20, 4))

    path = os.path.join(cfg.TESTING_DATA_DIR,
                        cfg.SIMULATION_NAME,
                        'driving_log.csv')
    data_df = pd.read_csv(path)

    cte_values = data_df["cte"]
    cte_values = np.convolve(cte_values, np.ones(15), 'valid') / 15

    x_losses = np.arange(len(cte_values))

    x_threshold = np.arange(len(cte_values))
    y_threshold = [cfg.CTE_TOLERANCE_LEVEL] * len(x_threshold)
    y_threshold_2 = [-cfg.CTE_TOLERANCE_LEVEL] * len(x_threshold)

    crashes = data_df[data_df["crashed"] == 1]
    is_crash = (crashes.crashed - 1) + cfg.CTE_TOLERANCE_LEVEL

    plt.plot(x_threshold, y_threshold, color='red', alpha=0.2)
    plt.plot(x_threshold, y_threshold_2, color='red', alpha=0.2)
    plt.plot(x_losses, cte_values, color=plt.jet(), alpha=0.7, label="cte")
    plt.plot(is_crash, 'bo', markersize=2)

    plt.legend()
    plt.ylabel('CTE')
    plt.xlabel('Frames')
    plt.title("CTE values for " + cfg.SIMULATION_NAME)

    # plt.savefig('plots/reconstruction-plot-' + name + '.png')

    plt.show()
