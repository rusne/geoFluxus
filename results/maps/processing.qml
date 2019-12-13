<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis simplifyMaxScale="1" labelsEnabled="0" simplifyAlgorithm="0" maxScale="0" simplifyDrawingTol="1" version="3.8.3-Zanzibar" minScale="1e+08" readOnly="0" styleCategories="AllStyleCategories" hasScaleBasedVisibilityFlag="0" simplifyDrawingHints="1" simplifyLocal="1">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
  </flags>
  <renderer-v2 symbollevels="0" enableorderby="0" attr="name" type="categorizedSymbol" forceraster="0">
    <categories>
      <category render="true" symbol="0" label="A01 Bewaren" value="A01 Bewaren"/>
      <category render="true" symbol="1" label="A02 Overslag / opbulken" value="A02 Overslag / opbulken"/>
      <category render="true" symbol="2" label="B03 Inzetten als bouwstof" value="B03 Inzetten als bouwstof"/>
      <category render="true" symbol="3" label="B04 Inzetten als brandstof" value="B04 Inzetten als brandstof"/>
      <category render="true" symbol="4" label="B05 Overig inzetten als grondstof" value="B05 Overig inzetten als grondstof"/>
      <category render="true" symbol="5" label="C01 Breken" value="C01 Breken"/>
      <category render="true" symbol="6" label="C02 Shredderen / knippen" value="C02 Shredderen / knippen"/>
      <category render="true" symbol="7" label="C03 Sorteren / scheiden" value="C03 Sorteren / scheiden"/>
      <category render="true" symbol="8" label="C04 Immobiliseren voor hergebruik" value="C04 Immobiliseren voor hergebruik"/>
      <category render="true" symbol="9" label="D01 Chemisch / fysisch scheiden" value="D01 Chemisch / fysisch scheiden"/>
      <category render="true" symbol="10" label="D04 Metaal terugwinnen (chemisch)" value="D04 Metaal terugwinnen (chemisch)"/>
      <category render="true" symbol="11" label="D05 Extractief reinigen (grond)" value="D05 Extractief reinigen (grond)"/>
      <category render="true" symbol="12" label="E01 Vergisten" value="E01 Vergisten"/>
      <category render="true" symbol="13" label="E02 Composteren, anaeroob" value="E02 Composteren, anaeroob"/>
      <category render="true" symbol="14" label="E03 Composteren, aeroob" value="E03 Composteren, aeroob"/>
      <category render="true" symbol="15" label="E04 Biologisch reinigen (water)" value="E04 Biologisch reinigen (water)"/>
      <category render="true" symbol="16" label="E05 Biologisch reinigen (grond)" value="E05 Biologisch reinigen (grond)"/>
      <category render="true" symbol="17" label="F01 Verbranden in roosterovens" value="F01 Verbranden in roosterovens"/>
      <category render="true" symbol="18" label="F03 Pyrolyse" value="F03 Pyrolyse"/>
      <category render="true" symbol="19" label="F05 Uitgloeien (grond)" value="F05 Uitgloeien (grond)"/>
      <category render="true" symbol="20" label="F07 Verbranden met terugwinnen energie (bijstoken)" value="F07 Verbranden met terugwinnen energie (bijstoken)"/>
      <category render="true" symbol="21" label="G01 Direct storten" value="G01 Direct storten"/>
      <category render="true" symbol="22" label="" value=""/>
    </categories>
    <symbols>
      <symbol alpha="1" clip_to_extent="1" type="line" force_rhr="0" name="0">
        <layer class="ArrowLine" locked="0" pass="0" enabled="1">
          <prop v="1" k="arrow_start_width"/>
          <prop v="MM" k="arrow_start_width_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="arrow_start_width_unit_scale"/>
          <prop v="0" k="arrow_type"/>
          <prop v="1" k="arrow_width"/>
          <prop v="MM" k="arrow_width_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="arrow_width_unit_scale"/>
          <prop v="1.5" k="head_length"/>
          <prop v="MM" k="head_length_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="head_length_unit_scale"/>
          <prop v="1.5" k="head_thickness"/>
          <prop v="MM" k="head_thickness_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="head_thickness_unit_scale"/>
          <prop v="0" k="head_type"/>
          <prop v="0" k="is_curved"/>
          <prop v="0" k="is_repeated"/>
          <prop v="0" k="offset"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_unit_scale"/>
          <prop v="0" k="ring_filter"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" value="" name="name"/>
              <Option type="Map" name="properties">
                <Option type="Map" name="arrowHeadLength">
                  <Option type="bool" value="true" name="active"/>
                  <Option type="QString" value="scale_linear(&quot;sum&quot;,0,10000,0.1,6) + 2" name="expression"/>
                  <Option type="int" value="3" name="type"/>
                </Option>
                <Option type="Map" name="arrowHeadThickness">
                  <Option type="bool" value="true" name="active"/>
                  <Option type="QString" value="scale_linear(&quot;sum&quot;,0,10000,0.1,6) + 2" name="expression"/>
                  <Option type="int" value="3" name="type"/>
                </Option>
                <Option type="Map" name="arrowStartWidth">
                  <Option type="bool" value="true" name="active"/>
                  <Option type="QString" value="scale_linear(&quot;sum&quot;,0,10000,0.1,6)" name="expression"/>
                  <Option type="int" value="3" name="type"/>
                </Option>
                <Option type="Map" name="arrowWidth">
                  <Option type="bool" value="true" name="active"/>
                  <Option type="QString" value="scale_linear(&quot;sum&quot;,0,10000,0.1,6)" name="expression"/>
                  <Option type="int" value="3" name="type"/>
                </Option>
              </Option>
              <Option type="QString" value="collection" name="type"/>
            </Option>
          </data_defined_properties>
          <symbol alpha="0.502" clip_to_extent="1" type="fill" force_rhr="0" name="@0@0">
            <layer class="SimpleFill" locked="0" pass="0" enabled="1">
              <prop v="3x:0,0,0,0,0,0" k="border_width_map_unit_scale"/>
              <prop v="68,1,84,255" k="color"/>
              <prop v="round" k="joinstyle"/>
              <prop v="0,0" k="offset"/>
              <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
              <prop v="MM" k="offset_unit"/>
              <prop v="190,178,151,255" k="outline_color"/>
              <prop v="no" k="outline_style"/>
              <prop v="0.26" k="outline_width"/>
              <prop v="MM" k="outline_width_unit"/>
              <prop v="solid" k="style"/>
              <data_defined_properties>
                <Option type="Map">
                  <Option type="QString" value="" name="name"/>
                  <Option name="properties"/>
                  <Option type="QString" value="collection" name="type"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol alpha="1" clip_to_extent="1" type="line" force_rhr="0" name="1">
        <layer class="ArrowLine" locked="0" pass="0" enabled="1">
          <prop v="1" k="arrow_start_width"/>
          <prop v="MM" k="arrow_start_width_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="arrow_start_width_unit_scale"/>
          <prop v="0" k="arrow_type"/>
          <prop v="1" k="arrow_width"/>
          <prop v="MM" k="arrow_width_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="arrow_width_unit_scale"/>
          <prop v="1.5" k="head_length"/>
          <prop v="MM" k="head_length_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="head_length_unit_scale"/>
          <prop v="1.5" k="head_thickness"/>
          <prop v="MM" k="head_thickness_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="head_thickness_unit_scale"/>
          <prop v="0" k="head_type"/>
          <prop v="0" k="is_curved"/>
          <prop v="0" k="is_repeated"/>
          <prop v="0" k="offset"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_unit_scale"/>
          <prop v="0" k="ring_filter"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" value="" name="name"/>
              <Option type="Map" name="properties">
                <Option type="Map" name="arrowHeadLength">
                  <Option type="bool" value="true" name="active"/>
                  <Option type="QString" value="scale_linear(&quot;sum&quot;,0,10000,0.1,6) + 2" name="expression"/>
                  <Option type="int" value="3" name="type"/>
                </Option>
                <Option type="Map" name="arrowHeadThickness">
                  <Option type="bool" value="true" name="active"/>
                  <Option type="QString" value="scale_linear(&quot;sum&quot;,0,10000,0.1,6) + 2" name="expression"/>
                  <Option type="int" value="3" name="type"/>
                </Option>
                <Option type="Map" name="arrowStartWidth">
                  <Option type="bool" value="true" name="active"/>
                  <Option type="QString" value="scale_linear(&quot;sum&quot;,0,10000,0.1,6)" name="expression"/>
                  <Option type="int" value="3" name="type"/>
                </Option>
                <Option type="Map" name="arrowWidth">
                  <Option type="bool" value="true" name="active"/>
                  <Option type="QString" value="scale_linear(&quot;sum&quot;,0,10000,0.1,6)" name="expression"/>
                  <Option type="int" value="3" name="type"/>
                </Option>
              </Option>
              <Option type="QString" value="collection" name="type"/>
            </Option>
          </data_defined_properties>
          <symbol alpha="0.502" clip_to_extent="1" type="fill" force_rhr="0" name="@1@0">
            <layer class="SimpleFill" locked="0" pass="0" enabled="1">
              <prop v="3x:0,0,0,0,0,0" k="border_width_map_unit_scale"/>
              <prop v="71,18,101,255" k="color"/>
              <prop v="round" k="joinstyle"/>
              <prop v="0,0" k="offset"/>
              <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
              <prop v="MM" k="offset_unit"/>
              <prop v="190,178,151,255" k="outline_color"/>
              <prop v="no" k="outline_style"/>
              <prop v="0.26" k="outline_width"/>
              <prop v="MM" k="outline_width_unit"/>
              <prop v="solid" k="style"/>
              <data_defined_properties>
                <Option type="Map">
                  <Option type="QString" value="" name="name"/>
                  <Option name="properties"/>
                  <Option type="QString" value="collection" name="type"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol alpha="1" clip_to_extent="1" type="line" force_rhr="0" name="10">
        <layer class="ArrowLine" locked="0" pass="0" enabled="1">
          <prop v="1" k="arrow_start_width"/>
          <prop v="MM" k="arrow_start_width_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="arrow_start_width_unit_scale"/>
          <prop v="0" k="arrow_type"/>
          <prop v="1" k="arrow_width"/>
          <prop v="MM" k="arrow_width_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="arrow_width_unit_scale"/>
          <prop v="1.5" k="head_length"/>
          <prop v="MM" k="head_length_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="head_length_unit_scale"/>
          <prop v="1.5" k="head_thickness"/>
          <prop v="MM" k="head_thickness_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="head_thickness_unit_scale"/>
          <prop v="0" k="head_type"/>
          <prop v="0" k="is_curved"/>
          <prop v="0" k="is_repeated"/>
          <prop v="0" k="offset"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_unit_scale"/>
          <prop v="0" k="ring_filter"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" value="" name="name"/>
              <Option type="Map" name="properties">
                <Option type="Map" name="arrowHeadLength">
                  <Option type="bool" value="true" name="active"/>
                  <Option type="QString" value="scale_linear(&quot;sum&quot;,0,10000,0.1,6) + 2" name="expression"/>
                  <Option type="int" value="3" name="type"/>
                </Option>
                <Option type="Map" name="arrowHeadThickness">
                  <Option type="bool" value="true" name="active"/>
                  <Option type="QString" value="scale_linear(&quot;sum&quot;,0,10000,0.1,6) + 2" name="expression"/>
                  <Option type="int" value="3" name="type"/>
                </Option>
                <Option type="Map" name="arrowStartWidth">
                  <Option type="bool" value="true" name="active"/>
                  <Option type="QString" value="scale_linear(&quot;sum&quot;,0,10000,0.1,6)" name="expression"/>
                  <Option type="int" value="3" name="type"/>
                </Option>
                <Option type="Map" name="arrowWidth">
                  <Option type="bool" value="true" name="active"/>
                  <Option type="QString" value="scale_linear(&quot;sum&quot;,0,10000,0.1,6)" name="expression"/>
                  <Option type="int" value="3" name="type"/>
                </Option>
              </Option>
              <Option type="QString" value="collection" name="type"/>
            </Option>
          </data_defined_properties>
          <symbol alpha="0.502" clip_to_extent="1" type="fill" force_rhr="0" name="@10@0">
            <layer class="SimpleFill" locked="0" pass="0" enabled="1">
              <prop v="3x:0,0,0,0,0,0" k="border_width_map_unit_scale"/>
              <prop v="36,133,142,255" k="color"/>
              <prop v="round" k="joinstyle"/>
              <prop v="0,0" k="offset"/>
              <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
              <prop v="MM" k="offset_unit"/>
              <prop v="190,178,151,255" k="outline_color"/>
              <prop v="no" k="outline_style"/>
              <prop v="0.26" k="outline_width"/>
              <prop v="MM" k="outline_width_unit"/>
              <prop v="solid" k="style"/>
              <data_defined_properties>
                <Option type="Map">
                  <Option type="QString" value="" name="name"/>
                  <Option name="properties"/>
                  <Option type="QString" value="collection" name="type"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol alpha="1" clip_to_extent="1" type="line" force_rhr="0" name="11">
        <layer class="ArrowLine" locked="0" pass="0" enabled="1">
          <prop v="1" k="arrow_start_width"/>
          <prop v="MM" k="arrow_start_width_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="arrow_start_width_unit_scale"/>
          <prop v="0" k="arrow_type"/>
          <prop v="1" k="arrow_width"/>
          <prop v="MM" k="arrow_width_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="arrow_width_unit_scale"/>
          <prop v="1.5" k="head_length"/>
          <prop v="MM" k="head_length_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="head_length_unit_scale"/>
          <prop v="1.5" k="head_thickness"/>
          <prop v="MM" k="head_thickness_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="head_thickness_unit_scale"/>
          <prop v="0" k="head_type"/>
          <prop v="0" k="is_curved"/>
          <prop v="0" k="is_repeated"/>
          <prop v="0" k="offset"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_unit_scale"/>
          <prop v="0" k="ring_filter"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" value="" name="name"/>
              <Option type="Map" name="properties">
                <Option type="Map" name="arrowHeadLength">
                  <Option type="bool" value="true" name="active"/>
                  <Option type="QString" value="scale_linear(&quot;sum&quot;,0,10000,0.1,6) + 2" name="expression"/>
                  <Option type="int" value="3" name="type"/>
                </Option>
                <Option type="Map" name="arrowHeadThickness">
                  <Option type="bool" value="true" name="active"/>
                  <Option type="QString" value="scale_linear(&quot;sum&quot;,0,10000,0.1,6) + 2" name="expression"/>
                  <Option type="int" value="3" name="type"/>
                </Option>
                <Option type="Map" name="arrowStartWidth">
                  <Option type="bool" value="true" name="active"/>
                  <Option type="QString" value="scale_linear(&quot;sum&quot;,0,10000,0.1,6)" name="expression"/>
                  <Option type="int" value="3" name="type"/>
                </Option>
                <Option type="Map" name="arrowWidth">
                  <Option type="bool" value="true" name="active"/>
                  <Option type="QString" value="scale_linear(&quot;sum&quot;,0,10000,0.1,6)" name="expression"/>
                  <Option type="int" value="3" name="type"/>
                </Option>
              </Option>
              <Option type="QString" value="collection" name="type"/>
            </Option>
          </data_defined_properties>
          <symbol alpha="0.502" clip_to_extent="1" type="fill" force_rhr="0" name="@11@0">
            <layer class="SimpleFill" locked="0" pass="0" enabled="1">
              <prop v="3x:0,0,0,0,0,0" k="border_width_map_unit_scale"/>
              <prop v="32,144,141,255" k="color"/>
              <prop v="round" k="joinstyle"/>
              <prop v="0,0" k="offset"/>
              <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
              <prop v="MM" k="offset_unit"/>
              <prop v="190,178,151,255" k="outline_color"/>
              <prop v="no" k="outline_style"/>
              <prop v="0.26" k="outline_width"/>
              <prop v="MM" k="outline_width_unit"/>
              <prop v="solid" k="style"/>
              <data_defined_properties>
                <Option type="Map">
                  <Option type="QString" value="" name="name"/>
                  <Option name="properties"/>
                  <Option type="QString" value="collection" name="type"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol alpha="1" clip_to_extent="1" type="line" force_rhr="0" name="12">
        <layer class="ArrowLine" locked="0" pass="0" enabled="1">
          <prop v="1" k="arrow_start_width"/>
          <prop v="MM" k="arrow_start_width_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="arrow_start_width_unit_scale"/>
          <prop v="0" k="arrow_type"/>
          <prop v="1" k="arrow_width"/>
          <prop v="MM" k="arrow_width_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="arrow_width_unit_scale"/>
          <prop v="1.5" k="head_length"/>
          <prop v="MM" k="head_length_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="head_length_unit_scale"/>
          <prop v="1.5" k="head_thickness"/>
          <prop v="MM" k="head_thickness_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="head_thickness_unit_scale"/>
          <prop v="0" k="head_type"/>
          <prop v="0" k="is_curved"/>
          <prop v="0" k="is_repeated"/>
          <prop v="0" k="offset"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_unit_scale"/>
          <prop v="0" k="ring_filter"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" value="" name="name"/>
              <Option type="Map" name="properties">
                <Option type="Map" name="arrowHeadLength">
                  <Option type="bool" value="true" name="active"/>
                  <Option type="QString" value="scale_linear(&quot;sum&quot;,0,10000,0.1,6) + 2" name="expression"/>
                  <Option type="int" value="3" name="type"/>
                </Option>
                <Option type="Map" name="arrowHeadThickness">
                  <Option type="bool" value="true" name="active"/>
                  <Option type="QString" value="scale_linear(&quot;sum&quot;,0,10000,0.1,6) + 2" name="expression"/>
                  <Option type="int" value="3" name="type"/>
                </Option>
                <Option type="Map" name="arrowStartWidth">
                  <Option type="bool" value="true" name="active"/>
                  <Option type="QString" value="scale_linear(&quot;sum&quot;,0,10000,0.1,6)" name="expression"/>
                  <Option type="int" value="3" name="type"/>
                </Option>
                <Option type="Map" name="arrowWidth">
                  <Option type="bool" value="true" name="active"/>
                  <Option type="QString" value="scale_linear(&quot;sum&quot;,0,10000,0.1,6)" name="expression"/>
                  <Option type="int" value="3" name="type"/>
                </Option>
              </Option>
              <Option type="QString" value="collection" name="type"/>
            </Option>
          </data_defined_properties>
          <symbol alpha="0.502" clip_to_extent="1" type="fill" force_rhr="0" name="@12@0">
            <layer class="SimpleFill" locked="0" pass="0" enabled="1">
              <prop v="3x:0,0,0,0,0,0" k="border_width_map_unit_scale"/>
              <prop v="30,155,137,255" k="color"/>
              <prop v="round" k="joinstyle"/>
              <prop v="0,0" k="offset"/>
              <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
              <prop v="MM" k="offset_unit"/>
              <prop v="190,178,151,255" k="outline_color"/>
              <prop v="no" k="outline_style"/>
              <prop v="0.26" k="outline_width"/>
              <prop v="MM" k="outline_width_unit"/>
              <prop v="solid" k="style"/>
              <data_defined_properties>
                <Option type="Map">
                  <Option type="QString" value="" name="name"/>
                  <Option name="properties"/>
                  <Option type="QString" value="collection" name="type"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol alpha="1" clip_to_extent="1" type="line" force_rhr="0" name="13">
        <layer class="ArrowLine" locked="0" pass="0" enabled="1">
          <prop v="1" k="arrow_start_width"/>
          <prop v="MM" k="arrow_start_width_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="arrow_start_width_unit_scale"/>
          <prop v="0" k="arrow_type"/>
          <prop v="1" k="arrow_width"/>
          <prop v="MM" k="arrow_width_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="arrow_width_unit_scale"/>
          <prop v="1.5" k="head_length"/>
          <prop v="MM" k="head_length_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="head_length_unit_scale"/>
          <prop v="1.5" k="head_thickness"/>
          <prop v="MM" k="head_thickness_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="head_thickness_unit_scale"/>
          <prop v="0" k="head_type"/>
          <prop v="0" k="is_curved"/>
          <prop v="0" k="is_repeated"/>
          <prop v="0" k="offset"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_unit_scale"/>
          <prop v="0" k="ring_filter"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" value="" name="name"/>
              <Option type="Map" name="properties">
                <Option type="Map" name="arrowHeadLength">
                  <Option type="bool" value="true" name="active"/>
                  <Option type="QString" value="scale_linear(&quot;sum&quot;,0,10000,0.1,6) + 2" name="expression"/>
                  <Option type="int" value="3" name="type"/>
                </Option>
                <Option type="Map" name="arrowHeadThickness">
                  <Option type="bool" value="true" name="active"/>
                  <Option type="QString" value="scale_linear(&quot;sum&quot;,0,10000,0.1,6) + 2" name="expression"/>
                  <Option type="int" value="3" name="type"/>
                </Option>
                <Option type="Map" name="arrowStartWidth">
                  <Option type="bool" value="true" name="active"/>
                  <Option type="QString" value="scale_linear(&quot;sum&quot;,0,10000,0.1,6)" name="expression"/>
                  <Option type="int" value="3" name="type"/>
                </Option>
                <Option type="Map" name="arrowWidth">
                  <Option type="bool" value="true" name="active"/>
                  <Option type="QString" value="scale_linear(&quot;sum&quot;,0,10000,0.1,6)" name="expression"/>
                  <Option type="int" value="3" name="type"/>
                </Option>
              </Option>
              <Option type="QString" value="collection" name="type"/>
            </Option>
          </data_defined_properties>
          <symbol alpha="0.502" clip_to_extent="1" type="fill" force_rhr="0" name="@13@0">
            <layer class="SimpleFill" locked="0" pass="0" enabled="1">
              <prop v="3x:0,0,0,0,0,0" k="border_width_map_unit_scale"/>
              <prop v="33,166,133,255" k="color"/>
              <prop v="round" k="joinstyle"/>
              <prop v="0,0" k="offset"/>
              <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
              <prop v="MM" k="offset_unit"/>
              <prop v="190,178,151,255" k="outline_color"/>
              <prop v="no" k="outline_style"/>
              <prop v="0.26" k="outline_width"/>
              <prop v="MM" k="outline_width_unit"/>
              <prop v="solid" k="style"/>
              <data_defined_properties>
                <Option type="Map">
                  <Option type="QString" value="" name="name"/>
                  <Option name="properties"/>
                  <Option type="QString" value="collection" name="type"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol alpha="1" clip_to_extent="1" type="line" force_rhr="0" name="14">
        <layer class="ArrowLine" locked="0" pass="0" enabled="1">
          <prop v="1" k="arrow_start_width"/>
          <prop v="MM" k="arrow_start_width_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="arrow_start_width_unit_scale"/>
          <prop v="0" k="arrow_type"/>
          <prop v="1" k="arrow_width"/>
          <prop v="MM" k="arrow_width_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="arrow_width_unit_scale"/>
          <prop v="1.5" k="head_length"/>
          <prop v="MM" k="head_length_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="head_length_unit_scale"/>
          <prop v="1.5" k="head_thickness"/>
          <prop v="MM" k="head_thickness_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="head_thickness_unit_scale"/>
          <prop v="0" k="head_type"/>
          <prop v="0" k="is_curved"/>
          <prop v="0" k="is_repeated"/>
          <prop v="0" k="offset"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_unit_scale"/>
          <prop v="0" k="ring_filter"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" value="" name="name"/>
              <Option type="Map" name="properties">
                <Option type="Map" name="arrowHeadLength">
                  <Option type="bool" value="true" name="active"/>
                  <Option type="QString" value="scale_linear(&quot;sum&quot;,0,10000,0.1,6) + 2" name="expression"/>
                  <Option type="int" value="3" name="type"/>
                </Option>
                <Option type="Map" name="arrowHeadThickness">
                  <Option type="bool" value="true" name="active"/>
                  <Option type="QString" value="scale_linear(&quot;sum&quot;,0,10000,0.1,6) + 2" name="expression"/>
                  <Option type="int" value="3" name="type"/>
                </Option>
                <Option type="Map" name="arrowStartWidth">
                  <Option type="bool" value="true" name="active"/>
                  <Option type="QString" value="scale_linear(&quot;sum&quot;,0,10000,0.1,6)" name="expression"/>
                  <Option type="int" value="3" name="type"/>
                </Option>
                <Option type="Map" name="arrowWidth">
                  <Option type="bool" value="true" name="active"/>
                  <Option type="QString" value="scale_linear(&quot;sum&quot;,0,10000,0.1,6)" name="expression"/>
                  <Option type="int" value="3" name="type"/>
                </Option>
              </Option>
              <Option type="QString" value="collection" name="type"/>
            </Option>
          </data_defined_properties>
          <symbol alpha="0.502" clip_to_extent="1" type="fill" force_rhr="0" name="@14@0">
            <layer class="SimpleFill" locked="0" pass="0" enabled="1">
              <prop v="3x:0,0,0,0,0,0" k="border_width_map_unit_scale"/>
              <prop v="42,176,126,255" k="color"/>
              <prop v="round" k="joinstyle"/>
              <prop v="0,0" k="offset"/>
              <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
              <prop v="MM" k="offset_unit"/>
              <prop v="190,178,151,255" k="outline_color"/>
              <prop v="no" k="outline_style"/>
              <prop v="0.26" k="outline_width"/>
              <prop v="MM" k="outline_width_unit"/>
              <prop v="solid" k="style"/>
              <data_defined_properties>
                <Option type="Map">
                  <Option type="QString" value="" name="name"/>
                  <Option name="properties"/>
                  <Option type="QString" value="collection" name="type"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol alpha="1" clip_to_extent="1" type="line" force_rhr="0" name="15">
        <layer class="ArrowLine" locked="0" pass="0" enabled="1">
          <prop v="1" k="arrow_start_width"/>
          <prop v="MM" k="arrow_start_width_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="arrow_start_width_unit_scale"/>
          <prop v="0" k="arrow_type"/>
          <prop v="1" k="arrow_width"/>
          <prop v="MM" k="arrow_width_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="arrow_width_unit_scale"/>
          <prop v="1.5" k="head_length"/>
          <prop v="MM" k="head_length_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="head_length_unit_scale"/>
          <prop v="1.5" k="head_thickness"/>
          <prop v="MM" k="head_thickness_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="head_thickness_unit_scale"/>
          <prop v="0" k="head_type"/>
          <prop v="0" k="is_curved"/>
          <prop v="0" k="is_repeated"/>
          <prop v="0" k="offset"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_unit_scale"/>
          <prop v="0" k="ring_filter"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" value="" name="name"/>
              <Option type="Map" name="properties">
                <Option type="Map" name="arrowHeadLength">
                  <Option type="bool" value="true" name="active"/>
                  <Option type="QString" value="scale_linear(&quot;sum&quot;,0,10000,0.1,6) + 2" name="expression"/>
                  <Option type="int" value="3" name="type"/>
                </Option>
                <Option type="Map" name="arrowHeadThickness">
                  <Option type="bool" value="true" name="active"/>
                  <Option type="QString" value="scale_linear(&quot;sum&quot;,0,10000,0.1,6) + 2" name="expression"/>
                  <Option type="int" value="3" name="type"/>
                </Option>
                <Option type="Map" name="arrowStartWidth">
                  <Option type="bool" value="true" name="active"/>
                  <Option type="QString" value="scale_linear(&quot;sum&quot;,0,10000,0.1,6)" name="expression"/>
                  <Option type="int" value="3" name="type"/>
                </Option>
                <Option type="Map" name="arrowWidth">
                  <Option type="bool" value="true" name="active"/>
                  <Option type="QString" value="scale_linear(&quot;sum&quot;,0,10000,0.1,6)" name="expression"/>
                  <Option type="int" value="3" name="type"/>
                </Option>
              </Option>
              <Option type="QString" value="collection" name="type"/>
            </Option>
          </data_defined_properties>
          <symbol alpha="0.502" clip_to_extent="1" type="fill" force_rhr="0" name="@15@0">
            <layer class="SimpleFill" locked="0" pass="0" enabled="1">
              <prop v="3x:0,0,0,0,0,0" k="border_width_map_unit_scale"/>
              <prop v="59,187,117,255" k="color"/>
              <prop v="round" k="joinstyle"/>
              <prop v="0,0" k="offset"/>
              <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
              <prop v="MM" k="offset_unit"/>
              <prop v="190,178,151,255" k="outline_color"/>
              <prop v="no" k="outline_style"/>
              <prop v="0.26" k="outline_width"/>
              <prop v="MM" k="outline_width_unit"/>
              <prop v="solid" k="style"/>
              <data_defined_properties>
                <Option type="Map">
                  <Option type="QString" value="" name="name"/>
                  <Option name="properties"/>
                  <Option type="QString" value="collection" name="type"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol alpha="1" clip_to_extent="1" type="line" force_rhr="0" name="16">
        <layer class="ArrowLine" locked="0" pass="0" enabled="1">
          <prop v="1" k="arrow_start_width"/>
          <prop v="MM" k="arrow_start_width_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="arrow_start_width_unit_scale"/>
          <prop v="0" k="arrow_type"/>
          <prop v="1" k="arrow_width"/>
          <prop v="MM" k="arrow_width_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="arrow_width_unit_scale"/>
          <prop v="1.5" k="head_length"/>
          <prop v="MM" k="head_length_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="head_length_unit_scale"/>
          <prop v="1.5" k="head_thickness"/>
          <prop v="MM" k="head_thickness_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="head_thickness_unit_scale"/>
          <prop v="0" k="head_type"/>
          <prop v="0" k="is_curved"/>
          <prop v="0" k="is_repeated"/>
          <prop v="0" k="offset"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_unit_scale"/>
          <prop v="0" k="ring_filter"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" value="" name="name"/>
              <Option type="Map" name="properties">
                <Option type="Map" name="arrowHeadLength">
                  <Option type="bool" value="true" name="active"/>
                  <Option type="QString" value="scale_linear(&quot;sum&quot;,0,10000,0.1,6) + 2" name="expression"/>
                  <Option type="int" value="3" name="type"/>
                </Option>
                <Option type="Map" name="arrowHeadThickness">
                  <Option type="bool" value="true" name="active"/>
                  <Option type="QString" value="scale_linear(&quot;sum&quot;,0,10000,0.1,6) + 2" name="expression"/>
                  <Option type="int" value="3" name="type"/>
                </Option>
                <Option type="Map" name="arrowStartWidth">
                  <Option type="bool" value="true" name="active"/>
                  <Option type="QString" value="scale_linear(&quot;sum&quot;,0,10000,0.1,6)" name="expression"/>
                  <Option type="int" value="3" name="type"/>
                </Option>
                <Option type="Map" name="arrowWidth">
                  <Option type="bool" value="true" name="active"/>
                  <Option type="QString" value="scale_linear(&quot;sum&quot;,0,10000,0.1,6)" name="expression"/>
                  <Option type="int" value="3" name="type"/>
                </Option>
              </Option>
              <Option type="QString" value="collection" name="type"/>
            </Option>
          </data_defined_properties>
          <symbol alpha="0.502" clip_to_extent="1" type="fill" force_rhr="0" name="@16@0">
            <layer class="SimpleFill" locked="0" pass="0" enabled="1">
              <prop v="3x:0,0,0,0,0,0" k="border_width_map_unit_scale"/>
              <prop v="81,197,105,255" k="color"/>
              <prop v="round" k="joinstyle"/>
              <prop v="0,0" k="offset"/>
              <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
              <prop v="MM" k="offset_unit"/>
              <prop v="190,178,151,255" k="outline_color"/>
              <prop v="no" k="outline_style"/>
              <prop v="0.26" k="outline_width"/>
              <prop v="MM" k="outline_width_unit"/>
              <prop v="solid" k="style"/>
              <data_defined_properties>
                <Option type="Map">
                  <Option type="QString" value="" name="name"/>
                  <Option name="properties"/>
                  <Option type="QString" value="collection" name="type"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol alpha="1" clip_to_extent="1" type="line" force_rhr="0" name="17">
        <layer class="ArrowLine" locked="0" pass="0" enabled="1">
          <prop v="1" k="arrow_start_width"/>
          <prop v="MM" k="arrow_start_width_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="arrow_start_width_unit_scale"/>
          <prop v="0" k="arrow_type"/>
          <prop v="1" k="arrow_width"/>
          <prop v="MM" k="arrow_width_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="arrow_width_unit_scale"/>
          <prop v="1.5" k="head_length"/>
          <prop v="MM" k="head_length_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="head_length_unit_scale"/>
          <prop v="1.5" k="head_thickness"/>
          <prop v="MM" k="head_thickness_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="head_thickness_unit_scale"/>
          <prop v="0" k="head_type"/>
          <prop v="0" k="is_curved"/>
          <prop v="0" k="is_repeated"/>
          <prop v="0" k="offset"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_unit_scale"/>
          <prop v="0" k="ring_filter"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" value="" name="name"/>
              <Option type="Map" name="properties">
                <Option type="Map" name="arrowHeadLength">
                  <Option type="bool" value="true" name="active"/>
                  <Option type="QString" value="scale_linear(&quot;sum&quot;,0,10000,0.1,6) + 2" name="expression"/>
                  <Option type="int" value="3" name="type"/>
                </Option>
                <Option type="Map" name="arrowHeadThickness">
                  <Option type="bool" value="true" name="active"/>
                  <Option type="QString" value="scale_linear(&quot;sum&quot;,0,10000,0.1,6) + 2" name="expression"/>
                  <Option type="int" value="3" name="type"/>
                </Option>
                <Option type="Map" name="arrowStartWidth">
                  <Option type="bool" value="true" name="active"/>
                  <Option type="QString" value="scale_linear(&quot;sum&quot;,0,10000,0.1,6)" name="expression"/>
                  <Option type="int" value="3" name="type"/>
                </Option>
                <Option type="Map" name="arrowWidth">
                  <Option type="bool" value="true" name="active"/>
                  <Option type="QString" value="scale_linear(&quot;sum&quot;,0,10000,0.1,6)" name="expression"/>
                  <Option type="int" value="3" name="type"/>
                </Option>
              </Option>
              <Option type="QString" value="collection" name="type"/>
            </Option>
          </data_defined_properties>
          <symbol alpha="0.502" clip_to_extent="1" type="fill" force_rhr="0" name="@17@0">
            <layer class="SimpleFill" locked="0" pass="0" enabled="1">
              <prop v="3x:0,0,0,0,0,0" k="border_width_map_unit_scale"/>
              <prop v="105,205,91,255" k="color"/>
              <prop v="round" k="joinstyle"/>
              <prop v="0,0" k="offset"/>
              <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
              <prop v="MM" k="offset_unit"/>
              <prop v="190,178,151,255" k="outline_color"/>
              <prop v="no" k="outline_style"/>
              <prop v="0.26" k="outline_width"/>
              <prop v="MM" k="outline_width_unit"/>
              <prop v="solid" k="style"/>
              <data_defined_properties>
                <Option type="Map">
                  <Option type="QString" value="" name="name"/>
                  <Option name="properties"/>
                  <Option type="QString" value="collection" name="type"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol alpha="1" clip_to_extent="1" type="line" force_rhr="0" name="18">
        <layer class="ArrowLine" locked="0" pass="0" enabled="1">
          <prop v="1" k="arrow_start_width"/>
          <prop v="MM" k="arrow_start_width_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="arrow_start_width_unit_scale"/>
          <prop v="0" k="arrow_type"/>
          <prop v="1" k="arrow_width"/>
          <prop v="MM" k="arrow_width_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="arrow_width_unit_scale"/>
          <prop v="1.5" k="head_length"/>
          <prop v="MM" k="head_length_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="head_length_unit_scale"/>
          <prop v="1.5" k="head_thickness"/>
          <prop v="MM" k="head_thickness_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="head_thickness_unit_scale"/>
          <prop v="0" k="head_type"/>
          <prop v="0" k="is_curved"/>
          <prop v="0" k="is_repeated"/>
          <prop v="0" k="offset"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_unit_scale"/>
          <prop v="0" k="ring_filter"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" value="" name="name"/>
              <Option type="Map" name="properties">
                <Option type="Map" name="arrowHeadLength">
                  <Option type="bool" value="true" name="active"/>
                  <Option type="QString" value="scale_linear(&quot;sum&quot;,0,10000,0.1,6) + 2" name="expression"/>
                  <Option type="int" value="3" name="type"/>
                </Option>
                <Option type="Map" name="arrowHeadThickness">
                  <Option type="bool" value="true" name="active"/>
                  <Option type="QString" value="scale_linear(&quot;sum&quot;,0,10000,0.1,6) + 2" name="expression"/>
                  <Option type="int" value="3" name="type"/>
                </Option>
                <Option type="Map" name="arrowStartWidth">
                  <Option type="bool" value="true" name="active"/>
                  <Option type="QString" value="scale_linear(&quot;sum&quot;,0,10000,0.1,6)" name="expression"/>
                  <Option type="int" value="3" name="type"/>
                </Option>
                <Option type="Map" name="arrowWidth">
                  <Option type="bool" value="true" name="active"/>
                  <Option type="QString" value="scale_linear(&quot;sum&quot;,0,10000,0.1,6)" name="expression"/>
                  <Option type="int" value="3" name="type"/>
                </Option>
              </Option>
              <Option type="QString" value="collection" name="type"/>
            </Option>
          </data_defined_properties>
          <symbol alpha="0.502" clip_to_extent="1" type="fill" force_rhr="0" name="@18@0">
            <layer class="SimpleFill" locked="0" pass="0" enabled="1">
              <prop v="3x:0,0,0,0,0,0" k="border_width_map_unit_scale"/>
              <prop v="133,213,74,255" k="color"/>
              <prop v="round" k="joinstyle"/>
              <prop v="0,0" k="offset"/>
              <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
              <prop v="MM" k="offset_unit"/>
              <prop v="190,178,151,255" k="outline_color"/>
              <prop v="no" k="outline_style"/>
              <prop v="0.26" k="outline_width"/>
              <prop v="MM" k="outline_width_unit"/>
              <prop v="solid" k="style"/>
              <data_defined_properties>
                <Option type="Map">
                  <Option type="QString" value="" name="name"/>
                  <Option name="properties"/>
                  <Option type="QString" value="collection" name="type"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol alpha="1" clip_to_extent="1" type="line" force_rhr="0" name="19">
        <layer class="ArrowLine" locked="0" pass="0" enabled="1">
          <prop v="1" k="arrow_start_width"/>
          <prop v="MM" k="arrow_start_width_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="arrow_start_width_unit_scale"/>
          <prop v="0" k="arrow_type"/>
          <prop v="1" k="arrow_width"/>
          <prop v="MM" k="arrow_width_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="arrow_width_unit_scale"/>
          <prop v="1.5" k="head_length"/>
          <prop v="MM" k="head_length_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="head_length_unit_scale"/>
          <prop v="1.5" k="head_thickness"/>
          <prop v="MM" k="head_thickness_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="head_thickness_unit_scale"/>
          <prop v="0" k="head_type"/>
          <prop v="0" k="is_curved"/>
          <prop v="0" k="is_repeated"/>
          <prop v="0" k="offset"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_unit_scale"/>
          <prop v="0" k="ring_filter"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" value="" name="name"/>
              <Option type="Map" name="properties">
                <Option type="Map" name="arrowHeadLength">
                  <Option type="bool" value="true" name="active"/>
                  <Option type="QString" value="scale_linear(&quot;sum&quot;,0,10000,0.1,6) + 2" name="expression"/>
                  <Option type="int" value="3" name="type"/>
                </Option>
                <Option type="Map" name="arrowHeadThickness">
                  <Option type="bool" value="true" name="active"/>
                  <Option type="QString" value="scale_linear(&quot;sum&quot;,0,10000,0.1,6) + 2" name="expression"/>
                  <Option type="int" value="3" name="type"/>
                </Option>
                <Option type="Map" name="arrowStartWidth">
                  <Option type="bool" value="true" name="active"/>
                  <Option type="QString" value="scale_linear(&quot;sum&quot;,0,10000,0.1,6)" name="expression"/>
                  <Option type="int" value="3" name="type"/>
                </Option>
                <Option type="Map" name="arrowWidth">
                  <Option type="bool" value="true" name="active"/>
                  <Option type="QString" value="scale_linear(&quot;sum&quot;,0,10000,0.1,6)" name="expression"/>
                  <Option type="int" value="3" name="type"/>
                </Option>
              </Option>
              <Option type="QString" value="collection" name="type"/>
            </Option>
          </data_defined_properties>
          <symbol alpha="0.502" clip_to_extent="1" type="fill" force_rhr="0" name="@19@0">
            <layer class="SimpleFill" locked="0" pass="0" enabled="1">
              <prop v="3x:0,0,0,0,0,0" k="border_width_map_unit_scale"/>
              <prop v="163,218,54,255" k="color"/>
              <prop v="round" k="joinstyle"/>
              <prop v="0,0" k="offset"/>
              <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
              <prop v="MM" k="offset_unit"/>
              <prop v="190,178,151,255" k="outline_color"/>
              <prop v="no" k="outline_style"/>
              <prop v="0.26" k="outline_width"/>
              <prop v="MM" k="outline_width_unit"/>
              <prop v="solid" k="style"/>
              <data_defined_properties>
                <Option type="Map">
                  <Option type="QString" value="" name="name"/>
                  <Option name="properties"/>
                  <Option type="QString" value="collection" name="type"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol alpha="1" clip_to_extent="1" type="line" force_rhr="0" name="2">
        <layer class="ArrowLine" locked="0" pass="0" enabled="1">
          <prop v="1" k="arrow_start_width"/>
          <prop v="MM" k="arrow_start_width_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="arrow_start_width_unit_scale"/>
          <prop v="0" k="arrow_type"/>
          <prop v="1" k="arrow_width"/>
          <prop v="MM" k="arrow_width_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="arrow_width_unit_scale"/>
          <prop v="1.5" k="head_length"/>
          <prop v="MM" k="head_length_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="head_length_unit_scale"/>
          <prop v="1.5" k="head_thickness"/>
          <prop v="MM" k="head_thickness_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="head_thickness_unit_scale"/>
          <prop v="0" k="head_type"/>
          <prop v="0" k="is_curved"/>
          <prop v="0" k="is_repeated"/>
          <prop v="0" k="offset"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_unit_scale"/>
          <prop v="0" k="ring_filter"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" value="" name="name"/>
              <Option type="Map" name="properties">
                <Option type="Map" name="arrowHeadLength">
                  <Option type="bool" value="true" name="active"/>
                  <Option type="QString" value="scale_linear(&quot;sum&quot;,0,10000,0.1,6) + 2" name="expression"/>
                  <Option type="int" value="3" name="type"/>
                </Option>
                <Option type="Map" name="arrowHeadThickness">
                  <Option type="bool" value="true" name="active"/>
                  <Option type="QString" value="scale_linear(&quot;sum&quot;,0,10000,0.1,6) + 2" name="expression"/>
                  <Option type="int" value="3" name="type"/>
                </Option>
                <Option type="Map" name="arrowStartWidth">
                  <Option type="bool" value="true" name="active"/>
                  <Option type="QString" value="scale_linear(&quot;sum&quot;,0,10000,0.1,6)" name="expression"/>
                  <Option type="int" value="3" name="type"/>
                </Option>
                <Option type="Map" name="arrowWidth">
                  <Option type="bool" value="true" name="active"/>
                  <Option type="QString" value="scale_linear(&quot;sum&quot;,0,10000,0.1,6)" name="expression"/>
                  <Option type="int" value="3" name="type"/>
                </Option>
              </Option>
              <Option type="QString" value="collection" name="type"/>
            </Option>
          </data_defined_properties>
          <symbol alpha="0.502" clip_to_extent="1" type="fill" force_rhr="0" name="@2@0">
            <layer class="SimpleFill" locked="0" pass="0" enabled="1">
              <prop v="3x:0,0,0,0,0,0" k="border_width_map_unit_scale"/>
              <prop v="72,33,115,255" k="color"/>
              <prop v="round" k="joinstyle"/>
              <prop v="0,0" k="offset"/>
              <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
              <prop v="MM" k="offset_unit"/>
              <prop v="190,178,151,255" k="outline_color"/>
              <prop v="no" k="outline_style"/>
              <prop v="0.26" k="outline_width"/>
              <prop v="MM" k="outline_width_unit"/>
              <prop v="solid" k="style"/>
              <data_defined_properties>
                <Option type="Map">
                  <Option type="QString" value="" name="name"/>
                  <Option name="properties"/>
                  <Option type="QString" value="collection" name="type"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol alpha="1" clip_to_extent="1" type="line" force_rhr="0" name="20">
        <layer class="ArrowLine" locked="0" pass="0" enabled="1">
          <prop v="1" k="arrow_start_width"/>
          <prop v="MM" k="arrow_start_width_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="arrow_start_width_unit_scale"/>
          <prop v="0" k="arrow_type"/>
          <prop v="1" k="arrow_width"/>
          <prop v="MM" k="arrow_width_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="arrow_width_unit_scale"/>
          <prop v="1.5" k="head_length"/>
          <prop v="MM" k="head_length_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="head_length_unit_scale"/>
          <prop v="1.5" k="head_thickness"/>
          <prop v="MM" k="head_thickness_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="head_thickness_unit_scale"/>
          <prop v="0" k="head_type"/>
          <prop v="0" k="is_curved"/>
          <prop v="0" k="is_repeated"/>
          <prop v="0" k="offset"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_unit_scale"/>
          <prop v="0" k="ring_filter"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" value="" name="name"/>
              <Option type="Map" name="properties">
                <Option type="Map" name="arrowHeadLength">
                  <Option type="bool" value="true" name="active"/>
                  <Option type="QString" value="scale_linear(&quot;sum&quot;,0,10000,0.1,6) + 2" name="expression"/>
                  <Option type="int" value="3" name="type"/>
                </Option>
                <Option type="Map" name="arrowHeadThickness">
                  <Option type="bool" value="true" name="active"/>
                  <Option type="QString" value="scale_linear(&quot;sum&quot;,0,10000,0.1,6) + 2" name="expression"/>
                  <Option type="int" value="3" name="type"/>
                </Option>
                <Option type="Map" name="arrowStartWidth">
                  <Option type="bool" value="true" name="active"/>
                  <Option type="QString" value="scale_linear(&quot;sum&quot;,0,10000,0.1,6)" name="expression"/>
                  <Option type="int" value="3" name="type"/>
                </Option>
                <Option type="Map" name="arrowWidth">
                  <Option type="bool" value="true" name="active"/>
                  <Option type="QString" value="scale_linear(&quot;sum&quot;,0,10000,0.1,6)" name="expression"/>
                  <Option type="int" value="3" name="type"/>
                </Option>
              </Option>
              <Option type="QString" value="collection" name="type"/>
            </Option>
          </data_defined_properties>
          <symbol alpha="0.502" clip_to_extent="1" type="fill" force_rhr="0" name="@20@0">
            <layer class="SimpleFill" locked="0" pass="0" enabled="1">
              <prop v="3x:0,0,0,0,0,0" k="border_width_map_unit_scale"/>
              <prop v="194,224,35,255" k="color"/>
              <prop v="round" k="joinstyle"/>
              <prop v="0,0" k="offset"/>
              <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
              <prop v="MM" k="offset_unit"/>
              <prop v="190,178,151,255" k="outline_color"/>
              <prop v="no" k="outline_style"/>
              <prop v="0.26" k="outline_width"/>
              <prop v="MM" k="outline_width_unit"/>
              <prop v="solid" k="style"/>
              <data_defined_properties>
                <Option type="Map">
                  <Option type="QString" value="" name="name"/>
                  <Option name="properties"/>
                  <Option type="QString" value="collection" name="type"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol alpha="1" clip_to_extent="1" type="line" force_rhr="0" name="21">
        <layer class="ArrowLine" locked="0" pass="0" enabled="1">
          <prop v="1" k="arrow_start_width"/>
          <prop v="MM" k="arrow_start_width_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="arrow_start_width_unit_scale"/>
          <prop v="0" k="arrow_type"/>
          <prop v="1" k="arrow_width"/>
          <prop v="MM" k="arrow_width_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="arrow_width_unit_scale"/>
          <prop v="1.5" k="head_length"/>
          <prop v="MM" k="head_length_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="head_length_unit_scale"/>
          <prop v="1.5" k="head_thickness"/>
          <prop v="MM" k="head_thickness_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="head_thickness_unit_scale"/>
          <prop v="0" k="head_type"/>
          <prop v="0" k="is_curved"/>
          <prop v="0" k="is_repeated"/>
          <prop v="0" k="offset"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_unit_scale"/>
          <prop v="0" k="ring_filter"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" value="" name="name"/>
              <Option type="Map" name="properties">
                <Option type="Map" name="arrowHeadLength">
                  <Option type="bool" value="true" name="active"/>
                  <Option type="QString" value="scale_linear(&quot;sum&quot;,0,10000,0.1,6) + 2" name="expression"/>
                  <Option type="int" value="3" name="type"/>
                </Option>
                <Option type="Map" name="arrowHeadThickness">
                  <Option type="bool" value="true" name="active"/>
                  <Option type="QString" value="scale_linear(&quot;sum&quot;,0,10000,0.1,6) + 2" name="expression"/>
                  <Option type="int" value="3" name="type"/>
                </Option>
                <Option type="Map" name="arrowStartWidth">
                  <Option type="bool" value="true" name="active"/>
                  <Option type="QString" value="scale_linear(&quot;sum&quot;,0,10000,0.1,6)" name="expression"/>
                  <Option type="int" value="3" name="type"/>
                </Option>
                <Option type="Map" name="arrowWidth">
                  <Option type="bool" value="true" name="active"/>
                  <Option type="QString" value="scale_linear(&quot;sum&quot;,0,10000,0.1,6)" name="expression"/>
                  <Option type="int" value="3" name="type"/>
                </Option>
              </Option>
              <Option type="QString" value="collection" name="type"/>
            </Option>
          </data_defined_properties>
          <symbol alpha="0.502" clip_to_extent="1" type="fill" force_rhr="0" name="@21@0">
            <layer class="SimpleFill" locked="0" pass="0" enabled="1">
              <prop v="3x:0,0,0,0,0,0" k="border_width_map_unit_scale"/>
              <prop v="225,228,25,255" k="color"/>
              <prop v="round" k="joinstyle"/>
              <prop v="0,0" k="offset"/>
              <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
              <prop v="MM" k="offset_unit"/>
              <prop v="190,178,151,255" k="outline_color"/>
              <prop v="no" k="outline_style"/>
              <prop v="0.26" k="outline_width"/>
              <prop v="MM" k="outline_width_unit"/>
              <prop v="solid" k="style"/>
              <data_defined_properties>
                <Option type="Map">
                  <Option type="QString" value="" name="name"/>
                  <Option name="properties"/>
                  <Option type="QString" value="collection" name="type"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol alpha="1" clip_to_extent="1" type="line" force_rhr="0" name="22">
        <layer class="ArrowLine" locked="0" pass="0" enabled="1">
          <prop v="1" k="arrow_start_width"/>
          <prop v="MM" k="arrow_start_width_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="arrow_start_width_unit_scale"/>
          <prop v="0" k="arrow_type"/>
          <prop v="1" k="arrow_width"/>
          <prop v="MM" k="arrow_width_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="arrow_width_unit_scale"/>
          <prop v="1.5" k="head_length"/>
          <prop v="MM" k="head_length_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="head_length_unit_scale"/>
          <prop v="1.5" k="head_thickness"/>
          <prop v="MM" k="head_thickness_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="head_thickness_unit_scale"/>
          <prop v="0" k="head_type"/>
          <prop v="0" k="is_curved"/>
          <prop v="0" k="is_repeated"/>
          <prop v="0" k="offset"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_unit_scale"/>
          <prop v="0" k="ring_filter"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" value="" name="name"/>
              <Option type="Map" name="properties">
                <Option type="Map" name="arrowHeadLength">
                  <Option type="bool" value="true" name="active"/>
                  <Option type="QString" value="scale_linear(&quot;sum&quot;,0,10000,0.1,6) + 2" name="expression"/>
                  <Option type="int" value="3" name="type"/>
                </Option>
                <Option type="Map" name="arrowHeadThickness">
                  <Option type="bool" value="true" name="active"/>
                  <Option type="QString" value="scale_linear(&quot;sum&quot;,0,10000,0.1,6) + 2" name="expression"/>
                  <Option type="int" value="3" name="type"/>
                </Option>
                <Option type="Map" name="arrowStartWidth">
                  <Option type="bool" value="true" name="active"/>
                  <Option type="QString" value="scale_linear(&quot;sum&quot;,0,10000,0.1,6)" name="expression"/>
                  <Option type="int" value="3" name="type"/>
                </Option>
                <Option type="Map" name="arrowWidth">
                  <Option type="bool" value="true" name="active"/>
                  <Option type="QString" value="scale_linear(&quot;sum&quot;,0,10000,0.1,6)" name="expression"/>
                  <Option type="int" value="3" name="type"/>
                </Option>
              </Option>
              <Option type="QString" value="collection" name="type"/>
            </Option>
          </data_defined_properties>
          <symbol alpha="0.502" clip_to_extent="1" type="fill" force_rhr="0" name="@22@0">
            <layer class="SimpleFill" locked="0" pass="0" enabled="1">
              <prop v="3x:0,0,0,0,0,0" k="border_width_map_unit_scale"/>
              <prop v="253,231,37,255" k="color"/>
              <prop v="round" k="joinstyle"/>
              <prop v="0,0" k="offset"/>
              <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
              <prop v="MM" k="offset_unit"/>
              <prop v="190,178,151,255" k="outline_color"/>
              <prop v="no" k="outline_style"/>
              <prop v="0.26" k="outline_width"/>
              <prop v="MM" k="outline_width_unit"/>
              <prop v="solid" k="style"/>
              <data_defined_properties>
                <Option type="Map">
                  <Option type="QString" value="" name="name"/>
                  <Option name="properties"/>
                  <Option type="QString" value="collection" name="type"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol alpha="1" clip_to_extent="1" type="line" force_rhr="0" name="3">
        <layer class="ArrowLine" locked="0" pass="0" enabled="1">
          <prop v="1" k="arrow_start_width"/>
          <prop v="MM" k="arrow_start_width_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="arrow_start_width_unit_scale"/>
          <prop v="0" k="arrow_type"/>
          <prop v="1" k="arrow_width"/>
          <prop v="MM" k="arrow_width_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="arrow_width_unit_scale"/>
          <prop v="1.5" k="head_length"/>
          <prop v="MM" k="head_length_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="head_length_unit_scale"/>
          <prop v="1.5" k="head_thickness"/>
          <prop v="MM" k="head_thickness_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="head_thickness_unit_scale"/>
          <prop v="0" k="head_type"/>
          <prop v="0" k="is_curved"/>
          <prop v="0" k="is_repeated"/>
          <prop v="0" k="offset"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_unit_scale"/>
          <prop v="0" k="ring_filter"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" value="" name="name"/>
              <Option type="Map" name="properties">
                <Option type="Map" name="arrowHeadLength">
                  <Option type="bool" value="true" name="active"/>
                  <Option type="QString" value="scale_linear(&quot;sum&quot;,0,10000,0.1,6) + 2" name="expression"/>
                  <Option type="int" value="3" name="type"/>
                </Option>
                <Option type="Map" name="arrowHeadThickness">
                  <Option type="bool" value="true" name="active"/>
                  <Option type="QString" value="scale_linear(&quot;sum&quot;,0,10000,0.1,6) + 2" name="expression"/>
                  <Option type="int" value="3" name="type"/>
                </Option>
                <Option type="Map" name="arrowStartWidth">
                  <Option type="bool" value="true" name="active"/>
                  <Option type="QString" value="scale_linear(&quot;sum&quot;,0,10000,0.1,6)" name="expression"/>
                  <Option type="int" value="3" name="type"/>
                </Option>
                <Option type="Map" name="arrowWidth">
                  <Option type="bool" value="true" name="active"/>
                  <Option type="QString" value="scale_linear(&quot;sum&quot;,0,10000,0.1,6)" name="expression"/>
                  <Option type="int" value="3" name="type"/>
                </Option>
              </Option>
              <Option type="QString" value="collection" name="type"/>
            </Option>
          </data_defined_properties>
          <symbol alpha="0.502" clip_to_extent="1" type="fill" force_rhr="0" name="@3@0">
            <layer class="SimpleFill" locked="0" pass="0" enabled="1">
              <prop v="3x:0,0,0,0,0,0" k="border_width_map_unit_scale"/>
              <prop v="70,47,126,255" k="color"/>
              <prop v="round" k="joinstyle"/>
              <prop v="0,0" k="offset"/>
              <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
              <prop v="MM" k="offset_unit"/>
              <prop v="190,178,151,255" k="outline_color"/>
              <prop v="no" k="outline_style"/>
              <prop v="0.26" k="outline_width"/>
              <prop v="MM" k="outline_width_unit"/>
              <prop v="solid" k="style"/>
              <data_defined_properties>
                <Option type="Map">
                  <Option type="QString" value="" name="name"/>
                  <Option name="properties"/>
                  <Option type="QString" value="collection" name="type"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol alpha="1" clip_to_extent="1" type="line" force_rhr="0" name="4">
        <layer class="ArrowLine" locked="0" pass="0" enabled="1">
          <prop v="1" k="arrow_start_width"/>
          <prop v="MM" k="arrow_start_width_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="arrow_start_width_unit_scale"/>
          <prop v="0" k="arrow_type"/>
          <prop v="1" k="arrow_width"/>
          <prop v="MM" k="arrow_width_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="arrow_width_unit_scale"/>
          <prop v="1.5" k="head_length"/>
          <prop v="MM" k="head_length_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="head_length_unit_scale"/>
          <prop v="1.5" k="head_thickness"/>
          <prop v="MM" k="head_thickness_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="head_thickness_unit_scale"/>
          <prop v="0" k="head_type"/>
          <prop v="0" k="is_curved"/>
          <prop v="0" k="is_repeated"/>
          <prop v="0" k="offset"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_unit_scale"/>
          <prop v="0" k="ring_filter"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" value="" name="name"/>
              <Option type="Map" name="properties">
                <Option type="Map" name="arrowHeadLength">
                  <Option type="bool" value="true" name="active"/>
                  <Option type="QString" value="scale_linear(&quot;sum&quot;,0,10000,0.1,6) + 2" name="expression"/>
                  <Option type="int" value="3" name="type"/>
                </Option>
                <Option type="Map" name="arrowHeadThickness">
                  <Option type="bool" value="true" name="active"/>
                  <Option type="QString" value="scale_linear(&quot;sum&quot;,0,10000,0.1,6) + 2" name="expression"/>
                  <Option type="int" value="3" name="type"/>
                </Option>
                <Option type="Map" name="arrowStartWidth">
                  <Option type="bool" value="true" name="active"/>
                  <Option type="QString" value="scale_linear(&quot;sum&quot;,0,10000,0.1,6)" name="expression"/>
                  <Option type="int" value="3" name="type"/>
                </Option>
                <Option type="Map" name="arrowWidth">
                  <Option type="bool" value="true" name="active"/>
                  <Option type="QString" value="scale_linear(&quot;sum&quot;,0,10000,0.1,6)" name="expression"/>
                  <Option type="int" value="3" name="type"/>
                </Option>
              </Option>
              <Option type="QString" value="collection" name="type"/>
            </Option>
          </data_defined_properties>
          <symbol alpha="0.502" clip_to_extent="1" type="fill" force_rhr="0" name="@4@0">
            <layer class="SimpleFill" locked="0" pass="0" enabled="1">
              <prop v="3x:0,0,0,0,0,0" k="border_width_map_unit_scale"/>
              <prop v="66,62,133,255" k="color"/>
              <prop v="round" k="joinstyle"/>
              <prop v="0,0" k="offset"/>
              <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
              <prop v="MM" k="offset_unit"/>
              <prop v="190,178,151,255" k="outline_color"/>
              <prop v="no" k="outline_style"/>
              <prop v="0.26" k="outline_width"/>
              <prop v="MM" k="outline_width_unit"/>
              <prop v="solid" k="style"/>
              <data_defined_properties>
                <Option type="Map">
                  <Option type="QString" value="" name="name"/>
                  <Option name="properties"/>
                  <Option type="QString" value="collection" name="type"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol alpha="1" clip_to_extent="1" type="line" force_rhr="0" name="5">
        <layer class="ArrowLine" locked="0" pass="0" enabled="1">
          <prop v="1" k="arrow_start_width"/>
          <prop v="MM" k="arrow_start_width_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="arrow_start_width_unit_scale"/>
          <prop v="0" k="arrow_type"/>
          <prop v="1" k="arrow_width"/>
          <prop v="MM" k="arrow_width_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="arrow_width_unit_scale"/>
          <prop v="1.5" k="head_length"/>
          <prop v="MM" k="head_length_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="head_length_unit_scale"/>
          <prop v="1.5" k="head_thickness"/>
          <prop v="MM" k="head_thickness_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="head_thickness_unit_scale"/>
          <prop v="0" k="head_type"/>
          <prop v="0" k="is_curved"/>
          <prop v="0" k="is_repeated"/>
          <prop v="0" k="offset"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_unit_scale"/>
          <prop v="0" k="ring_filter"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" value="" name="name"/>
              <Option type="Map" name="properties">
                <Option type="Map" name="arrowHeadLength">
                  <Option type="bool" value="true" name="active"/>
                  <Option type="QString" value="scale_linear(&quot;sum&quot;,0,10000,0.1,6) + 2" name="expression"/>
                  <Option type="int" value="3" name="type"/>
                </Option>
                <Option type="Map" name="arrowHeadThickness">
                  <Option type="bool" value="true" name="active"/>
                  <Option type="QString" value="scale_linear(&quot;sum&quot;,0,10000,0.1,6) + 2" name="expression"/>
                  <Option type="int" value="3" name="type"/>
                </Option>
                <Option type="Map" name="arrowStartWidth">
                  <Option type="bool" value="true" name="active"/>
                  <Option type="QString" value="scale_linear(&quot;sum&quot;,0,10000,0.1,6)" name="expression"/>
                  <Option type="int" value="3" name="type"/>
                </Option>
                <Option type="Map" name="arrowWidth">
                  <Option type="bool" value="true" name="active"/>
                  <Option type="QString" value="scale_linear(&quot;sum&quot;,0,10000,0.1,6)" name="expression"/>
                  <Option type="int" value="3" name="type"/>
                </Option>
              </Option>
              <Option type="QString" value="collection" name="type"/>
            </Option>
          </data_defined_properties>
          <symbol alpha="0.502" clip_to_extent="1" type="fill" force_rhr="0" name="@5@0">
            <layer class="SimpleFill" locked="0" pass="0" enabled="1">
              <prop v="3x:0,0,0,0,0,0" k="border_width_map_unit_scale"/>
              <prop v="62,75,138,255" k="color"/>
              <prop v="round" k="joinstyle"/>
              <prop v="0,0" k="offset"/>
              <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
              <prop v="MM" k="offset_unit"/>
              <prop v="190,178,151,255" k="outline_color"/>
              <prop v="no" k="outline_style"/>
              <prop v="0.26" k="outline_width"/>
              <prop v="MM" k="outline_width_unit"/>
              <prop v="solid" k="style"/>
              <data_defined_properties>
                <Option type="Map">
                  <Option type="QString" value="" name="name"/>
                  <Option name="properties"/>
                  <Option type="QString" value="collection" name="type"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol alpha="1" clip_to_extent="1" type="line" force_rhr="0" name="6">
        <layer class="ArrowLine" locked="0" pass="0" enabled="1">
          <prop v="1" k="arrow_start_width"/>
          <prop v="MM" k="arrow_start_width_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="arrow_start_width_unit_scale"/>
          <prop v="0" k="arrow_type"/>
          <prop v="1" k="arrow_width"/>
          <prop v="MM" k="arrow_width_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="arrow_width_unit_scale"/>
          <prop v="1.5" k="head_length"/>
          <prop v="MM" k="head_length_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="head_length_unit_scale"/>
          <prop v="1.5" k="head_thickness"/>
          <prop v="MM" k="head_thickness_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="head_thickness_unit_scale"/>
          <prop v="0" k="head_type"/>
          <prop v="0" k="is_curved"/>
          <prop v="0" k="is_repeated"/>
          <prop v="0" k="offset"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_unit_scale"/>
          <prop v="0" k="ring_filter"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" value="" name="name"/>
              <Option type="Map" name="properties">
                <Option type="Map" name="arrowHeadLength">
                  <Option type="bool" value="true" name="active"/>
                  <Option type="QString" value="scale_linear(&quot;sum&quot;,0,10000,0.1,6) + 2" name="expression"/>
                  <Option type="int" value="3" name="type"/>
                </Option>
                <Option type="Map" name="arrowHeadThickness">
                  <Option type="bool" value="true" name="active"/>
                  <Option type="QString" value="scale_linear(&quot;sum&quot;,0,10000,0.1,6) + 2" name="expression"/>
                  <Option type="int" value="3" name="type"/>
                </Option>
                <Option type="Map" name="arrowStartWidth">
                  <Option type="bool" value="true" name="active"/>
                  <Option type="QString" value="scale_linear(&quot;sum&quot;,0,10000,0.1,6)" name="expression"/>
                  <Option type="int" value="3" name="type"/>
                </Option>
                <Option type="Map" name="arrowWidth">
                  <Option type="bool" value="true" name="active"/>
                  <Option type="QString" value="scale_linear(&quot;sum&quot;,0,10000,0.1,6)" name="expression"/>
                  <Option type="int" value="3" name="type"/>
                </Option>
              </Option>
              <Option type="QString" value="collection" name="type"/>
            </Option>
          </data_defined_properties>
          <symbol alpha="0.502" clip_to_extent="1" type="fill" force_rhr="0" name="@6@0">
            <layer class="SimpleFill" locked="0" pass="0" enabled="1">
              <prop v="3x:0,0,0,0,0,0" k="border_width_map_unit_scale"/>
              <prop v="56,88,140,255" k="color"/>
              <prop v="round" k="joinstyle"/>
              <prop v="0,0" k="offset"/>
              <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
              <prop v="MM" k="offset_unit"/>
              <prop v="190,178,151,255" k="outline_color"/>
              <prop v="no" k="outline_style"/>
              <prop v="0.26" k="outline_width"/>
              <prop v="MM" k="outline_width_unit"/>
              <prop v="solid" k="style"/>
              <data_defined_properties>
                <Option type="Map">
                  <Option type="QString" value="" name="name"/>
                  <Option name="properties"/>
                  <Option type="QString" value="collection" name="type"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol alpha="1" clip_to_extent="1" type="line" force_rhr="0" name="7">
        <layer class="ArrowLine" locked="0" pass="0" enabled="1">
          <prop v="1" k="arrow_start_width"/>
          <prop v="MM" k="arrow_start_width_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="arrow_start_width_unit_scale"/>
          <prop v="0" k="arrow_type"/>
          <prop v="1" k="arrow_width"/>
          <prop v="MM" k="arrow_width_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="arrow_width_unit_scale"/>
          <prop v="1.5" k="head_length"/>
          <prop v="MM" k="head_length_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="head_length_unit_scale"/>
          <prop v="1.5" k="head_thickness"/>
          <prop v="MM" k="head_thickness_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="head_thickness_unit_scale"/>
          <prop v="0" k="head_type"/>
          <prop v="0" k="is_curved"/>
          <prop v="0" k="is_repeated"/>
          <prop v="0" k="offset"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_unit_scale"/>
          <prop v="0" k="ring_filter"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" value="" name="name"/>
              <Option type="Map" name="properties">
                <Option type="Map" name="arrowHeadLength">
                  <Option type="bool" value="true" name="active"/>
                  <Option type="QString" value="scale_linear(&quot;sum&quot;,0,10000,0.1,6) + 2" name="expression"/>
                  <Option type="int" value="3" name="type"/>
                </Option>
                <Option type="Map" name="arrowHeadThickness">
                  <Option type="bool" value="true" name="active"/>
                  <Option type="QString" value="scale_linear(&quot;sum&quot;,0,10000,0.1,6) + 2" name="expression"/>
                  <Option type="int" value="3" name="type"/>
                </Option>
                <Option type="Map" name="arrowStartWidth">
                  <Option type="bool" value="true" name="active"/>
                  <Option type="QString" value="scale_linear(&quot;sum&quot;,0,10000,0.1,6)" name="expression"/>
                  <Option type="int" value="3" name="type"/>
                </Option>
                <Option type="Map" name="arrowWidth">
                  <Option type="bool" value="true" name="active"/>
                  <Option type="QString" value="scale_linear(&quot;sum&quot;,0,10000,0.1,6)" name="expression"/>
                  <Option type="int" value="3" name="type"/>
                </Option>
              </Option>
              <Option type="QString" value="collection" name="type"/>
            </Option>
          </data_defined_properties>
          <symbol alpha="0.502" clip_to_extent="1" type="fill" force_rhr="0" name="@7@0">
            <layer class="SimpleFill" locked="0" pass="0" enabled="1">
              <prop v="3x:0,0,0,0,0,0" k="border_width_map_unit_scale"/>
              <prop v="50,100,141,255" k="color"/>
              <prop v="round" k="joinstyle"/>
              <prop v="0,0" k="offset"/>
              <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
              <prop v="MM" k="offset_unit"/>
              <prop v="190,178,151,255" k="outline_color"/>
              <prop v="no" k="outline_style"/>
              <prop v="0.26" k="outline_width"/>
              <prop v="MM" k="outline_width_unit"/>
              <prop v="solid" k="style"/>
              <data_defined_properties>
                <Option type="Map">
                  <Option type="QString" value="" name="name"/>
                  <Option name="properties"/>
                  <Option type="QString" value="collection" name="type"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol alpha="1" clip_to_extent="1" type="line" force_rhr="0" name="8">
        <layer class="ArrowLine" locked="0" pass="0" enabled="1">
          <prop v="1" k="arrow_start_width"/>
          <prop v="MM" k="arrow_start_width_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="arrow_start_width_unit_scale"/>
          <prop v="0" k="arrow_type"/>
          <prop v="1" k="arrow_width"/>
          <prop v="MM" k="arrow_width_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="arrow_width_unit_scale"/>
          <prop v="1.5" k="head_length"/>
          <prop v="MM" k="head_length_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="head_length_unit_scale"/>
          <prop v="1.5" k="head_thickness"/>
          <prop v="MM" k="head_thickness_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="head_thickness_unit_scale"/>
          <prop v="0" k="head_type"/>
          <prop v="0" k="is_curved"/>
          <prop v="0" k="is_repeated"/>
          <prop v="0" k="offset"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_unit_scale"/>
          <prop v="0" k="ring_filter"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" value="" name="name"/>
              <Option type="Map" name="properties">
                <Option type="Map" name="arrowHeadLength">
                  <Option type="bool" value="true" name="active"/>
                  <Option type="QString" value="scale_linear(&quot;sum&quot;,0,10000,0.1,6) + 2" name="expression"/>
                  <Option type="int" value="3" name="type"/>
                </Option>
                <Option type="Map" name="arrowHeadThickness">
                  <Option type="bool" value="true" name="active"/>
                  <Option type="QString" value="scale_linear(&quot;sum&quot;,0,10000,0.1,6) + 2" name="expression"/>
                  <Option type="int" value="3" name="type"/>
                </Option>
                <Option type="Map" name="arrowStartWidth">
                  <Option type="bool" value="true" name="active"/>
                  <Option type="QString" value="scale_linear(&quot;sum&quot;,0,10000,0.1,6)" name="expression"/>
                  <Option type="int" value="3" name="type"/>
                </Option>
                <Option type="Map" name="arrowWidth">
                  <Option type="bool" value="true" name="active"/>
                  <Option type="QString" value="scale_linear(&quot;sum&quot;,0,10000,0.1,6)" name="expression"/>
                  <Option type="int" value="3" name="type"/>
                </Option>
              </Option>
              <Option type="QString" value="collection" name="type"/>
            </Option>
          </data_defined_properties>
          <symbol alpha="0.502" clip_to_extent="1" type="fill" force_rhr="0" name="@8@0">
            <layer class="SimpleFill" locked="0" pass="0" enabled="1">
              <prop v="3x:0,0,0,0,0,0" k="border_width_map_unit_scale"/>
              <prop v="45,111,142,255" k="color"/>
              <prop v="round" k="joinstyle"/>
              <prop v="0,0" k="offset"/>
              <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
              <prop v="MM" k="offset_unit"/>
              <prop v="190,178,151,255" k="outline_color"/>
              <prop v="no" k="outline_style"/>
              <prop v="0.26" k="outline_width"/>
              <prop v="MM" k="outline_width_unit"/>
              <prop v="solid" k="style"/>
              <data_defined_properties>
                <Option type="Map">
                  <Option type="QString" value="" name="name"/>
                  <Option name="properties"/>
                  <Option type="QString" value="collection" name="type"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol alpha="1" clip_to_extent="1" type="line" force_rhr="0" name="9">
        <layer class="ArrowLine" locked="0" pass="0" enabled="1">
          <prop v="1" k="arrow_start_width"/>
          <prop v="MM" k="arrow_start_width_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="arrow_start_width_unit_scale"/>
          <prop v="0" k="arrow_type"/>
          <prop v="1" k="arrow_width"/>
          <prop v="MM" k="arrow_width_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="arrow_width_unit_scale"/>
          <prop v="1.5" k="head_length"/>
          <prop v="MM" k="head_length_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="head_length_unit_scale"/>
          <prop v="1.5" k="head_thickness"/>
          <prop v="MM" k="head_thickness_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="head_thickness_unit_scale"/>
          <prop v="0" k="head_type"/>
          <prop v="0" k="is_curved"/>
          <prop v="0" k="is_repeated"/>
          <prop v="0" k="offset"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_unit_scale"/>
          <prop v="0" k="ring_filter"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" value="" name="name"/>
              <Option type="Map" name="properties">
                <Option type="Map" name="arrowHeadLength">
                  <Option type="bool" value="true" name="active"/>
                  <Option type="QString" value="scale_linear(&quot;sum&quot;,0,10000,0.1,6) + 2" name="expression"/>
                  <Option type="int" value="3" name="type"/>
                </Option>
                <Option type="Map" name="arrowHeadThickness">
                  <Option type="bool" value="true" name="active"/>
                  <Option type="QString" value="scale_linear(&quot;sum&quot;,0,10000,0.1,6) + 2" name="expression"/>
                  <Option type="int" value="3" name="type"/>
                </Option>
                <Option type="Map" name="arrowStartWidth">
                  <Option type="bool" value="true" name="active"/>
                  <Option type="QString" value="scale_linear(&quot;sum&quot;,0,10000,0.1,6)" name="expression"/>
                  <Option type="int" value="3" name="type"/>
                </Option>
                <Option type="Map" name="arrowWidth">
                  <Option type="bool" value="true" name="active"/>
                  <Option type="QString" value="scale_linear(&quot;sum&quot;,0,10000,0.1,6)" name="expression"/>
                  <Option type="int" value="3" name="type"/>
                </Option>
              </Option>
              <Option type="QString" value="collection" name="type"/>
            </Option>
          </data_defined_properties>
          <symbol alpha="0.502" clip_to_extent="1" type="fill" force_rhr="0" name="@9@0">
            <layer class="SimpleFill" locked="0" pass="0" enabled="1">
              <prop v="3x:0,0,0,0,0,0" k="border_width_map_unit_scale"/>
              <prop v="41,122,142,255" k="color"/>
              <prop v="round" k="joinstyle"/>
              <prop v="0,0" k="offset"/>
              <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
              <prop v="MM" k="offset_unit"/>
              <prop v="190,178,151,255" k="outline_color"/>
              <prop v="no" k="outline_style"/>
              <prop v="0.26" k="outline_width"/>
              <prop v="MM" k="outline_width_unit"/>
              <prop v="solid" k="style"/>
              <data_defined_properties>
                <Option type="Map">
                  <Option type="QString" value="" name="name"/>
                  <Option name="properties"/>
                  <Option type="QString" value="collection" name="type"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
      </symbol>
    </symbols>
    <source-symbol>
      <symbol alpha="1" clip_to_extent="1" type="line" force_rhr="0" name="0">
        <layer class="ArrowLine" locked="0" pass="0" enabled="1">
          <prop v="1" k="arrow_start_width"/>
          <prop v="MM" k="arrow_start_width_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="arrow_start_width_unit_scale"/>
          <prop v="0" k="arrow_type"/>
          <prop v="1" k="arrow_width"/>
          <prop v="MM" k="arrow_width_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="arrow_width_unit_scale"/>
          <prop v="1.5" k="head_length"/>
          <prop v="MM" k="head_length_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="head_length_unit_scale"/>
          <prop v="1.5" k="head_thickness"/>
          <prop v="MM" k="head_thickness_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="head_thickness_unit_scale"/>
          <prop v="0" k="head_type"/>
          <prop v="0" k="is_curved"/>
          <prop v="0" k="is_repeated"/>
          <prop v="0" k="offset"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_unit_scale"/>
          <prop v="0" k="ring_filter"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" value="" name="name"/>
              <Option type="Map" name="properties">
                <Option type="Map" name="arrowHeadLength">
                  <Option type="bool" value="true" name="active"/>
                  <Option type="QString" value="scale_linear(&quot;sum&quot;,0,10000,0.1,6) + 2" name="expression"/>
                  <Option type="int" value="3" name="type"/>
                </Option>
                <Option type="Map" name="arrowHeadThickness">
                  <Option type="bool" value="true" name="active"/>
                  <Option type="QString" value="scale_linear(&quot;sum&quot;,0,10000,0.1,6) + 2" name="expression"/>
                  <Option type="int" value="3" name="type"/>
                </Option>
                <Option type="Map" name="arrowStartWidth">
                  <Option type="bool" value="true" name="active"/>
                  <Option type="QString" value="scale_linear(&quot;sum&quot;,0,10000,0.1,6)" name="expression"/>
                  <Option type="int" value="3" name="type"/>
                </Option>
                <Option type="Map" name="arrowWidth">
                  <Option type="bool" value="true" name="active"/>
                  <Option type="QString" value="scale_linear(&quot;sum&quot;,0,10000,0.1,6)" name="expression"/>
                  <Option type="int" value="3" name="type"/>
                </Option>
              </Option>
              <Option type="QString" value="collection" name="type"/>
            </Option>
          </data_defined_properties>
          <symbol alpha="0.502" clip_to_extent="1" type="fill" force_rhr="0" name="@0@0">
            <layer class="SimpleFill" locked="0" pass="0" enabled="1">
              <prop v="3x:0,0,0,0,0,0" k="border_width_map_unit_scale"/>
              <prop v="0,0,0,255" k="color"/>
              <prop v="round" k="joinstyle"/>
              <prop v="0,0" k="offset"/>
              <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
              <prop v="MM" k="offset_unit"/>
              <prop v="190,178,151,255" k="outline_color"/>
              <prop v="no" k="outline_style"/>
              <prop v="0.26" k="outline_width"/>
              <prop v="MM" k="outline_width_unit"/>
              <prop v="solid" k="style"/>
              <data_defined_properties>
                <Option type="Map">
                  <Option type="QString" value="" name="name"/>
                  <Option name="properties"/>
                  <Option type="QString" value="collection" name="type"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
      </symbol>
    </source-symbol>
    <colorramp type="gradient" name="[source]">
      <prop v="68,1,84,255" k="color1"/>
      <prop v="253,231,37,255" k="color2"/>
      <prop v="0" k="discrete"/>
      <prop v="gradient" k="rampType"/>
      <prop v="0.0196078;70,8,92,255:0.0392157;71,16,99,255:0.0588235;72,23,105,255:0.0784314;72,29,111,255:0.0980392;72,36,117,255:0.117647;71,42,122,255:0.137255;70,48,126,255:0.156863;69,55,129,255:0.176471;67,61,132,255:0.196078;65,66,135,255:0.215686;63,72,137,255:0.235294;61,78,138,255:0.254902;58,83,139,255:0.27451;56,89,140,255:0.294118;53,94,141,255:0.313725;51,99,141,255:0.333333;49,104,142,255:0.352941;46,109,142,255:0.372549;44,113,142,255:0.392157;42,118,142,255:0.411765;41,123,142,255:0.431373;39,128,142,255:0.45098;37,132,142,255:0.470588;35,137,142,255:0.490196;33,142,141,255:0.509804;32,146,140,255:0.529412;31,151,139,255:0.54902;30,156,137,255:0.568627;31,161,136,255:0.588235;33,165,133,255:0.607843;36,170,131,255:0.627451;40,174,128,255:0.647059;46,179,124,255:0.666667;53,183,121,255:0.686275;61,188,116,255:0.705882;70,192,111,255:0.72549;80,196,106,255:0.745098;90,200,100,255:0.764706;101,203,94,255:0.784314;112,207,87,255:0.803922;124,210,80,255:0.823529;137,213,72,255:0.843137;149,216,64,255:0.862745;162,218,55,255:0.882353;176,221,47,255:0.901961;189,223,38,255:0.921569;202,225,31,255:0.941176;216,226,25,255:0.960784;229,228,25,255:0.980392;241,229,29,255" k="stops"/>
    </colorramp>
    <rotation/>
    <sizescale/>
  </renderer-v2>
  <customproperties>
    <property key="dualview/previewExpressions">
      <value>"name"</value>
    </property>
    <property key="embeddedWidgets/count" value="0"/>
    <property key="variableNames"/>
    <property key="variableValues"/>
  </customproperties>
  <blendMode>0</blendMode>
  <featureBlendMode>0</featureBlendMode>
  <layerOpacity>1</layerOpacity>
  <SingleCategoryDiagramRenderer attributeLegend="1" diagramType="Histogram">
    <DiagramCategory sizeType="MM" scaleDependency="Area" maxScaleDenominator="1e+08" penWidth="0" enabled="0" lineSizeType="MM" penColor="#000000" lineSizeScale="3x:0,0,0,0,0,0" labelPlacementMethod="XHeight" sizeScale="3x:0,0,0,0,0,0" width="15" diagramOrientation="Up" penAlpha="255" scaleBasedVisibility="0" height="15" minScaleDenominator="0" rotationOffset="270" barWidth="5" backgroundAlpha="255" opacity="1" backgroundColor="#ffffff" minimumSize="0">
      <fontProperties style="" description=".SF NS Text,13,-1,5,50,0,0,0,0,0"/>
    </DiagramCategory>
  </SingleCategoryDiagramRenderer>
  <DiagramLayerSettings dist="0" priority="0" linePlacementFlags="18" obstacle="0" showAll="1" zIndex="0" placement="2">
    <properties>
      <Option type="Map">
        <Option type="QString" value="" name="name"/>
        <Option name="properties"/>
        <Option type="QString" value="collection" name="type"/>
      </Option>
    </properties>
  </DiagramLayerSettings>
  <geometryOptions geometryPrecision="0" removeDuplicateNodes="0">
    <activeChecks/>
    <checkConfiguration/>
  </geometryOptions>
  <fieldConfiguration>
    <field name="_uid_">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="sum">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="keyflow_id">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="name">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
  </fieldConfiguration>
  <aliases>
    <alias index="0" field="_uid_" name=""/>
    <alias index="1" field="sum" name=""/>
    <alias index="2" field="keyflow_id" name=""/>
    <alias index="3" field="name" name=""/>
  </aliases>
  <excludeAttributesWMS/>
  <excludeAttributesWFS/>
  <defaults>
    <default applyOnUpdate="0" field="_uid_" expression=""/>
    <default applyOnUpdate="0" field="sum" expression=""/>
    <default applyOnUpdate="0" field="keyflow_id" expression=""/>
    <default applyOnUpdate="0" field="name" expression=""/>
  </defaults>
  <constraints>
    <constraint constraints="0" unique_strength="0" exp_strength="0" notnull_strength="0" field="_uid_"/>
    <constraint constraints="0" unique_strength="0" exp_strength="0" notnull_strength="0" field="sum"/>
    <constraint constraints="0" unique_strength="0" exp_strength="0" notnull_strength="0" field="keyflow_id"/>
    <constraint constraints="0" unique_strength="0" exp_strength="0" notnull_strength="0" field="name"/>
  </constraints>
  <constraintExpressions>
    <constraint exp="" desc="" field="_uid_"/>
    <constraint exp="" desc="" field="sum"/>
    <constraint exp="" desc="" field="keyflow_id"/>
    <constraint exp="" desc="" field="name"/>
  </constraintExpressions>
  <expressionfields/>
  <attributeactions>
    <defaultAction key="Canvas" value="{00000000-0000-0000-0000-000000000000}"/>
  </attributeactions>
  <attributetableconfig actionWidgetStyle="dropDown" sortOrder="0" sortExpression="&quot;keyflow_id&quot;">
    <columns>
      <column hidden="0" type="field" name="_uid_" width="-1"/>
      <column hidden="0" type="field" name="sum" width="-1"/>
      <column hidden="0" type="field" name="keyflow_id" width="-1"/>
      <column hidden="0" type="field" name="name" width="270"/>
      <column hidden="1" type="actions" width="-1"/>
    </columns>
  </attributetableconfig>
  <conditionalstyles>
    <rowstyles/>
    <fieldstyles/>
  </conditionalstyles>
  <editform tolerant="1"></editform>
  <editforminit/>
  <editforminitcodesource>0</editforminitcodesource>
  <editforminitfilepath></editforminitfilepath>
  <editforminitcode><![CDATA[# -*- coding: utf-8 -*-
"""
QGIS forms can have a Python function that is called when the form is
opened.

Use this function to add extra logic to your forms.

Enter the name of the function in the "Python Init function"
field.
An example follows:
"""
from qgis.PyQt.QtWidgets import QWidget

def my_form_open(dialog, layer, feature):
	geom = feature.geometry()
	control = dialog.findChild(QWidget, "MyLineEdit")
]]></editforminitcode>
  <featformsuppress>0</featformsuppress>
  <editorlayout>generatedlayout</editorlayout>
  <editable>
    <field editable="1" name="_uid_"/>
    <field editable="1" name="keyflow_id"/>
    <field editable="1" name="name"/>
    <field editable="1" name="sum"/>
  </editable>
  <labelOnTop>
    <field labelOnTop="0" name="_uid_"/>
    <field labelOnTop="0" name="keyflow_id"/>
    <field labelOnTop="0" name="name"/>
    <field labelOnTop="0" name="sum"/>
  </labelOnTop>
  <widgets/>
  <previewExpression>name</previewExpression>
  <mapTip></mapTip>
  <layerGeometryType>1</layerGeometryType>
</qgis>
