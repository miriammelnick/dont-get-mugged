
###############################################################################
#
# SpacialFeaturesSearch
# Searches for feature types within a specified bounding box.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class SpacialFeaturesSearch(Choreography):

    """
    Create a new instance of the SpacialFeaturesSearch Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/UnlockPlaces/SpacialFeaturesSearch')


    def new_input_set(self):
        return SpacialFeaturesSearchInputSet()

    def _make_result_set(self, result, path):
        return SpacialFeaturesSearchResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SpacialFeaturesSearchChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the SpacialFeaturesSearch
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class SpacialFeaturesSearchInputSet(InputSet):
        """
        Set the value of the FeatureType input for this choreography. ((string) The feature type that the place is (i.e. "Cities"). See http://unlock.edina.ac.uk/ws/supportedFeatureTypes?format=txt for a complete list of supported Feature Types.)
        """
        def set_FeatureType(self, value):
            InputSet._set_input(self, 'FeatureType', value)

        """
        Set the value of the Format input for this choreography. ((optional, string) The format of the place search results. One of xml, kml, json, georss or txt. Defaults to "xml".)
        """
        def set_Format(self, value):
            InputSet._set_input(self, 'Format', value)

        """
        Set the value of the Gazetteer input for this choreography. ((optional, string) The place-name source to take locations from. The options are geonames, os, naturalearth or unlock which combines all the previous. Defaults to "unlock".)
        """
        def set_Gazetteer(self, value):
            InputSet._set_input(self, 'Gazetteer', value)

        """
        Set the value of the MaxLatitude input for this choreography. ((decimal) The maximum latitude point of a bounding box.)
        """
        def set_MaxLatitude(self, value):
            InputSet._set_input(self, 'MaxLatitude', value)

        """
        Set the value of the MaxLongitude input for this choreography. ((decimal) The maximum longitude point of a bounding box.)
        """
        def set_MaxLongitude(self, value):
            InputSet._set_input(self, 'MaxLongitude', value)

        """
        Set the value of the MaxRows input for this choreography. ((optional, integer) The maximum number of results to return. Defaults to 20. Cannot exceed 1000.)
        """
        def set_MaxRows(self, value):
            InputSet._set_input(self, 'MaxRows', value)

        """
        Set the value of the MinLatitude input for this choreography. ((decimal) The minimum latitude point of a bounding box.)
        """
        def set_MinLatitude(self, value):
            InputSet._set_input(self, 'MinLatitude', value)

        """
        Set the value of the MinLongitude input for this choreography. ((decimal) The minimum longitude point of a bounding box.)
        """
        def set_MinLongitude(self, value):
            InputSet._set_input(self, 'MinLongitude', value)

        """
        Set the value of the Operator input for this choreography. (Valid values are: "within" and "intersect". The results will therefore be entirely within, or overlapping with (intersecting), the bounding box. Defaults to "within".)
        """
        def set_Operator(self, value):
            InputSet._set_input(self, 'Operator', value)

        """
        Set the value of the StartRow input for this choreography. ((optional, integer) The row to start results display from. Defaults to 1.)
        """
        def set_StartRow(self, value):
            InputSet._set_input(self, 'StartRow', value)


"""
A ResultSet with methods tailored to the values returned by the SpacialFeaturesSearch choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class SpacialFeaturesSearchResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((XML) The response from Unlock. Defaults to XML based on the format input parameter.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class SpacialFeaturesSearchChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SpacialFeaturesSearchResultSet(response, path)
