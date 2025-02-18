""" Portfolio Production Bot.
    This bot is used to produce a portfolio of betting.
    It is used to:
    1) Test the perfomance of a combination of strategies.
    2) Test the stats of a strategy with a portfolio.
    3) Run in real time.

    Here the configuration is done in the config_betting.yaml file.
    The configuration is done in the following way:
    1) The configuration is read from the config_betting.yaml file.
    2) The configuration is validated.
    3) The configuration is used to create the portfolio.
    4) The configuration is used to connect to the data source, run the simulation and run in real time
    to produce orders that will send to trading.
    """


def main(run_real : bool = False, send_orders_to_broker : bool = True) -> None:
    """ Run the portfolio engine. """
    from src.domain.config_helper import get_config
    import os
    from src.application.services.portfolio_constructor import Portfolio_Constructor
    path = os.path.abspath(__file__)
    path_bot = os.path.dirname(path)  # path to the module
    path_to_config = os.path.join(path_bot, "config_betting.yaml")
    conf_portfolio = get_config(path_to_config)  # get the configuration from the config file
    # run the portfolio engine, set run_real=True to run in real time

    portfolio_production = Portfolio_Constructor(conf_portfolio, run_real=run_real, asset_type='betting',
                                                 send_orders_to_broker=send_orders_to_broker)
    portfolio_production.run()


if __name__ == '__main__':
    main(run_real=True, send_orders_to_broker=True)

