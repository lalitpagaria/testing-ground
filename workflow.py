from obsei.configuration import ObseiConfiguration

obsei_configuration = ObseiConfiguration()

source_config = obsei_configuration.initialize_instance("source_config")
source = obsei_configuration.initialize_instance("source")

analyzer = obsei_configuration.initialize_instance("analyzer")
analyzer_config = obsei_configuration.initialize_instance("analyzer_config")

sink_config = obsei_configuration.initialize_instance("sink_config")
sink = obsei_configuration.initialize_instance("sink")

source_response_list = source.lookup(source_config)

analyzer_response_list = analyzer.analyze_input(
     source_response_list=source_response_list, analyzer_config=analyzer_config
)

sink_response_list = sink.send_data(analyzer_response_list, sink_config)