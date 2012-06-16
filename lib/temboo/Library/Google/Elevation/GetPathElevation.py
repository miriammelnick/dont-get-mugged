
###############################################################################
#
# GetPathElevation
# Obtain elevation information for a path specified by a set of  geo-coordinates.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetPathElevation(Choreography):

    """
    Create a new instance of the GetPathElevation Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Google/Elevation/GetPathElevation')


    def new_input_set(self):
        return GetPathElevationInputSet()

    def _make_result_set(self, result, path):
        return GetPathElevationResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetPathElevationChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetPathElevation
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetPathElevationInputSet(InputSet):
        """
        Set the value of the Path input for this choreography. ((required, string) Specify the path for which elevation data will be obtained.  Input formats: an array of two or more lat/longitude coordinate pairs; A set of encoded coordinates using the Encoded Polyline Algorithm.)
        """
        def set_Path(self, value):
            InputSet._set_input(self, 'Path', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) The format that response should be in. Can be set to xml or json. Defaults to json.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the Samples input for this choreography. ((required, integer) Enter the number of sample points.  See API docs for additional information.)
        """
        def set_Samples(self, value):
            InputSet._set_input(self, 'Samples', value)

        """
        Set the value of the Sensor input for this choreography. ((optional, boolean) Indicates whether or not the directions request is from a device with a location sensor. Value must be either 1 or 0. Defaults to 0 (false).)
        """
        def set_Sensor(self, value):
            InputSet._set_input(self, 'Sensor', value)


"""
A ResultSet with methods tailored to the values returned by the GetPathElevation choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetPathElevationResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Google.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetPathElevationChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetPathElevationResultSet(response, path)
